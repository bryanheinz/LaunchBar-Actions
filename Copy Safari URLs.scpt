tell application "Safari"
	set urlList to {}
	repeat with _tab in tabs of front window
		set end of urlList to URL of _tab
	end repeat
end tell
set urlString to urlList as string
set quoteURL to quoted form of urlString
do shell script "python <<EOF
var = " & quoteURL & "
var1 = var.split('http')
#print(var1[1:-1])
for _ in var1:
	if _:
		print('http' + _)
EOF"
set the clipboard to result