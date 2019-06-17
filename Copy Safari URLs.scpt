tell application "Safari"
    set urlList to {}
    repeat with _tab in tabs of front window
        set end of urlList to URL of _tab
    end repeat
end tell

set text item delimiters to "\n"
set theString to urlList as string

set the clipboard to theString