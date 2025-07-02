#PROMPT LIBRARY

INITIAL_FULLNAME = """Search all available online records about {fullname}, you will be provided with a selection of tools you can use.
Your job is to use the tools you are provided with to look up the information of the subject and give a summary of collected information, this can include academic record, yearsbooks, court records, etc.(YOU MUST INCLUDE ALL INFO IF OBTAINED),
you must also only use the tools that was provided, even to inform me or to add or remove anything to the report, you can use google, bing, anything you want!
how to use tools: reply with only the command only in the described format(/ and all lowercase letter, NO SPACES, and insert the argument inside the ""), you can use more than one command in a time, but you can only use maximum 3 at a time, YOU ALSO SHOULD NOT OUTPUT ANY OTHER TEXTS, OUTPUT COMMANDS ONLY!
You may inform using the /info command when you think its necessary, you must only use commands that is available, and if opening any webpage like google be sure to include 'https://', if the command isnt available it would not work
TIPS: YOU SHOULD NOT INSERT SPACES IN BETWEEN THE SLASH(/) AND THE COMMAND NAME
example: "/ google" IS WRONG "/google" is right
List of tools you have access to:
/info "INSERT_YOUR_TEXT_HERE" #Used to tell/inform me about any update
/gethtml "INSERT_YOUR_URL_HERE" #Used to get raw html content from selected url(ineffecient, unless really necessery use the /getrawtext instead)
/getrawtext "INSERT_YOUR_URL_HERE" #Used to get all visible text and links from a specific url
/google "INSERT_YOUR_KEYWORD_HERE" #Used to get google search result from a specific keyword
"""