$Date1 = Get-Date
function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
}
$IP = getIP
Write-Host("$IP")
$Body = "This Machines IP is $IP. User is $env:Username. Hostname is $env:ComputerName. Powershell Version 5. Today's date is $date1"

Send-MailMessage -To "bmtierney72@gmail.com" -from "bmtierney72@gmail.com" -Subject "IT3038C Windows Sysinfo" -Body $Body -SMTPServer smtp.gmail.com -Port 587 -useSSL -Credential (Get-Credential)