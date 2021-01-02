# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*

#### **1. costs**  
|VM|App Service|
|-----------|------------|
|cost may varies, depends on options |provides free tier for a year|  
| B1S machines will costs $0.0104/hour, $60.51/month | Basic, B1 will costs $73.65/month|


#### **2. Scalability**
|VM|App Service
|-----------|------------|
| VM scale sets| Built in service|
|Azure Load Balancer| Integrated | 
|Platform images: 1000 nodes per scale set, Custom images: 600 per nodes per scale set| 20 instances, 100 with App Service Environment|

#### **3. availability**
|VM|App Service
|-----------|------------|
|Broad range of VM SLAs: from single-instance at 99.9%| Achieve high availability with SLA-backed uptime of 99.95%
|Traffic manager | Traffic manager|


#### **4. workflow**
|VM|App Service
|-----------|------------|
| Create VM | Create WebService|
| Create SSH connection with the VM | Deploy Web App from Github |
| Install Web Server|
| Deploy Web Application | 
|Use public IP address to view web| Navigate to the deployed URL| 


#### **AppService deployment solutions:**
1. Create "Web App" on the azure portal
2. Setting configurations:
    + resource-group
    + web app name
    + publish: Code
    + Runtime stack: python 3.7
    + Operating System: Linux
    + Region
    + App Service Plan
    + SKU and size: F1 (free tier)
3. Deploy the App Service Web App
    + deploy the Web app from GitHub on Azure portal>Deployment Center
4. Navigate to the deployed URL


#### My Choice: 
I chose App Service since CMS App is a lightweight and won't approach to the size limit for App Services easily. Moreover, faster deployments than VM since App Service only requires fewer steps to deploy a Web Application. VM needs more customization in order to run an App. However, the CMS App has simple functions which only requires basic environment settings which already managed in App Service.


### Assess app changes that would change your decision.
If the CMS App has the potential that needs more features to be added with vast increase in Users, I will change my decision and chose VM.
Since VM allows to have the full access and control, I can optimize and chose various specs in order to meet the future requirements. Moreover, if the App need for dedicated servers for security reasons, the VM will be the better option to chose.



##### **Reference:
##### https://docs.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree
>>>>>>> 6bb6742ba8fdd05c4fe45fe34fed7126033d38e3
