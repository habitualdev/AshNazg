# AshNazg

- Often I find myself using strings to start my search for bad when doing malware/host analysis.
-This means waitng on strings itself, then waiting on grep to do it's buisness.
- So what if we keep everything in memory?

- AshNazg dumps everything into a redis database.
- Data structure is as follows:
  - \<STRING> : \<LINE NUMBER\>.\<STRING IN LINE NUMBER\>
  - Ex: The string "IamBAD" on line 306, the third identified string in that line would be IamBAD:306.3
  - Data is structured as such to inform follow on searchs

# Requirements
- Local redis DB accessible at 127.0.0.1 on the default port
- redis python library installed
