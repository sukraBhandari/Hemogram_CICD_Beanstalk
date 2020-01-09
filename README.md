Hemogram - Web application for reading Pheripheral Blood smears remotely
===

I migrated Hemogram application from Heroku platform to AWS Elastic Beanstalk. Here I am going to discuss how I deployed Hemogram application to Beanstalk using command line interface(CLI). Finally, I will also created a AWS CodePipeLine to automate the software release to Elastic Beanstalk.

Hemogram to Elastic Beanstalk
-----------------------------

Create application environment and deploy configured applicaiton to Elastic Beanstalk
- Intialize EB CLI repository with the be init command
```
C:\Desktop\hemogram-eb>eb init -p python-3.6 hemogram-aws --region us-west-2
Application hemogram-aws has been created.
```
The above command create a new application name hemogram-aws

- Run eb init again to configure a keypair for ec2 instance
```
C:\Desktop\hemogram-eb>eb init
Cannot setup CodeCommit because there is no Source Control setup, continuing with initialization
Do you want to set up SSH for your instances?
(Y/n): Y

Select a keypair.
1) demo-key
2) eb-test
3) edx-6.20.19
4) edx_key
5) guru-wp
6) lynda-test-6-19
7) private-key
8) [ Create new KeyPair ]
(default is 7): 1
```

- Create an environment and deploy Hemogram application to it with eb create. This step can take upto 5 minutes, because several resources are being created under the hood. EC2 instance,  instance security group, Load Balancer, Load Balancer security group, Auto Scaling group, Amazon S3 bucket, Amazon CloudWatch Alarms and CloudFormation Stack.
```
C:\Desktop\hemogram-eb>eb create hemogram-env
Creating application version archive "app-200109_124938".
Uploading hemogram-aws/app-200109_124938.zip to S3. This may take a while.
Upload Complete.
.
.
Successfully launched environment: hemogram-env
```
- Now the following line of code will open the application using application domain name
```
C:\Desktop\hemogram-eb>eb open
```
![eb_open](https://user-images.githubusercontent.com/7229266/72113315-edb9b080-32f4-11ea-9022-22a1e8e2344f.JPG)

AWS CodePipeline through console
-----------------------------
1. Create a CodeCommit repository
2. Push application code from your local repository to remote CodeCommit repository.
   Enter your username and password for the Git credentials.
3. Create a CodePipeline
4. Select source provider - AWS CodeCommit
5. Select repository and branch name
6. Skip the build stage for now
7. Select the deploy state - AWS Elastic Beanstalk
8. Select the Application name - hemogram-aws
9. Select the Environment name - Hemogram-env
10. Review and Create Pipeline.

![codepipe](https://user-images.githubusercontent.com/7229266/72113377-1e99e580-32f5-11ea-93db-8b37d54ee793.JPG)

**Author:**
---
Sukra Bhandari

