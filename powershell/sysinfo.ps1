$IP = Get-NetIPAddress | Where-Object {$_.IPv4Address -like '192*'}
$HOSTNAME = (Get-WmiObject -class Win32_ComputerSystem -Property Name).Name

$Body = "This Machine's IP is {0}" -f $IP.IPv4Address

$email = "alecnader@gmail.com" 
 
$pass = "" 
 
$smtpServer = "smtp.gmail.com" 
 
 
$msg = new-object Net.Mail.MailMessage 
$smtp = new-object Net.Mail.SmtpClient($smtpServer) 
$smtp.EnableSsl = $true 
$msg.From = "$email"  
$msg.To.Add("$email") 
$msg.BodyEncoding = [system.Text.Encoding]::Unicode 
$msg.SubjectEncoding = [system.Text.Encoding]::Unicode 
$msg.IsBodyHTML = $true  
$msg.Subject = "Naderaj-Win10" 
$msg.Body = "The name of this machine is:"+ $HOSTNAME+" This Machine's IP is {0}" -f $IP.IPv4Address
$SMTP.Credentials = New-Object System.Net.NetworkCredential("$email", "$pass"); 
$smtp.Send($msg)