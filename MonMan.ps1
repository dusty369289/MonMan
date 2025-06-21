$tvmonOB = Get-DisplayInfo | Where-Object -Property DisplayName -EQ 'SAMSUNG'
#$othermonsOB = Get-DisplayInfo | Where-Object -Property DisplayName -EQ "PL2280H"
if ($tvmonOB.Active){
    Disable-Display $tvmonOB.DisplayId
}else {
    Enable-Display $tvmonOB.DisplayId
}