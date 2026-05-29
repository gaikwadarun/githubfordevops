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

#AWS S3 
-simple storage service
-storge data in the form of objects
-we can store any type of data .csv .txt.mp4.mp3 
-widely used AWS service 
-different type of S3 bucket :
  -standerd -mostly used and recommended 
  -standerd IF
  -glacier IF

static website deployment on S3
-bucket Policy
-bucket permission
-kms-encryption

