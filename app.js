async function getApiData(apiEndpoint, apiKey, headers){
    if (!apiEndpoint.startsWith('/')) {
        apiEndpoint = '/' + apiEndpoint;
    }
    const proxyUrl = `http://localhost:3000${apiEndpoint}`; 
    try {
        const response = await fetch(proxyUrl, {
            method: 'GET',
            headers: headers,
        });

        if (!response.ok) {
            let errorMessage = `API request failed with status ${response.status}`;
            try {
                const errorData = await response.json();
                errorMessage += `: ${errorData.error}`;
            } catch (e) {}
            throw new Error(errorMessage);
        }
        return await response.json();

    } catch (error) {
        console.error('Error in getApiData:', error);
        throw error; //Re-throw the error to be handled by checkThreat
    }
}

function isValidIp(ip) {
    const ipv4Regex = /^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
    const ipv6Regex = /^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$/;
    return ipv4Regex.test(ip) || ipv6Regex.test(ip);
}

function isValidHash(hash) {
    const md5Regex = /^[a-f0-9]{32}$/i; // Case-insensitive MD5
    const sha1Regex = /^[a-f0-9]{40}$/i; // Case-insensitive SHA1
    const sha256Regex = /^[a-f0-9]{64}$/i; // Case-insensitive SHA256

    return md5Regex.test(hash) || sha1Regex.test(hash) || sha256Regex.test(hash);
}

function isValidUrl(url) {
    try {
        // More robust URL validation using the URL constructor
        const urlObj = new URL(url);
        // Add additional checks here if needed (e.g., protocol, domain)
        return true;
    } catch (error) {
        return false;
    }
}

async function checkThreat() {
    const inputType = document.getElementById('inputType').value;
    const inputValue = document.getElementById('inputValue').value;
    const resultsDiv = document.getElementById('results');
    const historyDiv = document.getElementById('history');
    resultsDiv.innerText = "Checking...";

    // Input Validation (Expand this significantly!)
    if (!inputValue) {
        resultsDiv.innerText = 'Please enter a value.';
        return;
    }

    let isValid = false;
    let errorMessage = "";

    if (inputType === "ip") {
        isValid = isValidIp(inputValue);
        errorMessage = "Invalid IP address format.";
    } else if (inputType === "hash") {
        isValid = isValidHash(inputValue);
        errorMessage = "Invalid hash format.";
    } else if (inputType === "url") {
        isValid = isValidUrl(inputValue);
        errorMessage = "Invalid URL format.";
    } else {
        resultsDiv.innerText = "Invalid Input Type";
        return;
    }

    if (!isValid) {
        resultsDiv.innerText = errorMessage;
        return;
    }

    let apiEndpoint;
    let apiKey = "AIzaSyDTXgONdt0aKqN4J_zStuTuZj5fmML7lY4"; // Replace with your actual API key (do NOT hardcode in production)
    let data;
    let result;
    let headers;

    try{
        if (inputType === 'ip') {
            apiEndpoint = `https://api.abuseipdb.com/api/v2/check?ipAddress=${inputValue}`;
            headers = {
                'Key': apiKey,
                'Accept': 'application/json'
            }
        } else if (inputType === 'hash') {
            apiEndpoint = `https://www.virustotal.com/api/v3/files/${inputValue}`;
            headers = {
                'x-apikey': apiKey,
                'Accept': 'application/json'
            }
        } else if (inputType === 'url') {
            apiEndpoint = `https://www.virustotal.com/api/v3/urls/${inputValue}`;
            headers = {
                'x-apikey': apiKey,
                'Accept': 'application/json'
            }
        } else { //handle text input
            resultsDiv.innerText = "Text input not yet implemented";
            return;
        }
        
        data = await getApiData(apiEndpoint, apiKey, headers);
        if(inputType === "ip"){
            result = `IP: ${data.data.ipAddress} is malicious: ${data.data.isMalicious}`;
        }else if(inputType === "hash"){
            result = `Hash: ${data.data.id} reputation: ${data.data.attributes.reputation}`;
        }else if (inputType === "url"){
            result = `URL: ${inputValue} reputation: ${data.data.attributes.last_analysis_stats.malicious}`;
        }

        //Update History
        historyDiv.innerHTML += `<p>${inputValue} : ${result}</p>`;
        resultsDiv.innerText = result;

    } catch (error) {
        resultsDiv.innerText = `Error: ${error.message}`;
        console.error("Error during API call:", error);
    }
}
