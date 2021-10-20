# Errors

The Sieve API uses the following error codes:

Error Code | Meaning
---------- | -------
200 | OK
400 | Bad Request -- Your request is invalid.
401 | Unauthorized -- Your API key is wrong.
403 | Forbidden -- The project requested is hidden for administrators only or doesn't exist.
406 | Not Acceptable -- You requested a format that isn't json.
429 | Too Many Requests -- You're sending images too quickly! Slow down!
500 | Internal Server Error -- We had a problem with our server. Try again later.
503 | Service Unavailable -- We're temporarily offline for maintenance. Please try again later.
