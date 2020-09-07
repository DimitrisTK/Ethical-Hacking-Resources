# **Web Applications Vulnerabilities**
Description & Exploit Techniques

## LFI
Using LFI an attacker can retrieve files from the local server also he can execute files of the local server thereby gaining shell of the victim machine.

__*Vulnerability fix:*__ Before using files in include file functionality,user input should be properly validated and functionality should be designed in such a way that user-controllable data does not need to be passed to filesystem operations.

 **How to Exploit:**

## RFI
Using RFI an attacker can execute files from the remote server.Remote File Inclusion allows us to execute a malicious shell hosted by a remote server by including it and thereby gaining shell of the victim machine.

__*Vulnerability fix:*__ Never use arbitrary input data in a file include request, or build a dynamic file inclusion whitelist.

 **How to Exploit:**

## Path Traversal - Directory Traversal
Allows an attacker to retrieve files from the local server.It is similar to LFI except the file execution.
It can fetch us information such as application code and data, credentials for back-end systems, and sensitive operating system files. Leveraging this information an attacker can ultimately gain full control of the server.For example if backend system is remotely accessible with credentials found by retrieving some configuration file then an attacker could have full control on the database.

__*Vulnerability fix:*__ Proper implementation of access control list for the directories in web server.

 **How to Exploit:**

## Prototype Pollution Attack
## Session Hijacking Attack
## Path Hijacking

## Top web application security risks (by OWASP)
### Injection


 **How to Exploit:**

## Broken authentication

 **How to Exploit:**

## Sensitive data exposure

 **How to Exploit:**

## XML external entities (XXE)

 **How to Exploit:**

## Broken access control

 **How to Exploit:**

## Security misconfiguration

 **How to Exploit:**

## Cross-site scripting (XSS)

 **How to Exploit:**

## Insecure deserialization

 **How to Exploit:**

## Using components with known vulnerabilities

 **How to Exploit:**

## Insufficient logging and monitoring

 **How to Exploit:**
