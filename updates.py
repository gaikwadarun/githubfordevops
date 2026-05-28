git stash 
git rebase
git diff
gitignore
conflict
git rebase
git reset

# AWS assumerole or cross account 
- Mostly we use for taking temporary access to the another account 
- it is valid for 1 hour or 12hr according to our Requirements
- process for assigning assumerole
suppose we have Account A and account B
 - we want to access account B
 - we have ro login into account B
 - create a role(eg. S3 full access or EC2 full access)
 - attach Policy
 -provide ARN which is account B's created role 
 -then connection will be establish 

