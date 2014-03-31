on handle_string(theCommand)
	do shell script "man -t " & theCommand & " | open -f -a /Applications/Preview.app"
end handle_string