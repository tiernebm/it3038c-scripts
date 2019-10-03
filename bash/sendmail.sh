BODY="User: \t $USER \n HOSTNAME: $HOSTNAME"

Send -MailMessage -To "botheaj@ucmail.uc.edu" -From "tiernebm@mail.uc.edu" -Subject "IT3038C Windows Sysinfo" -Body $BODY -SMTPServer smtp.office365.com -port 587 -UseSSL -Credential
