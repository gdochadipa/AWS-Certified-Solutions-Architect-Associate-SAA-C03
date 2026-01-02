# AWS Flashcards - Quick Memorization Guide

## 🎴 Service Categories at a Glance

### Compute Services
```
┌─────────────────────────────────────────┐
│ EC2         → Virtual Servers           │
│ Lambda      → Serverless Functions      │
│ ECS/EKS     → Container Orchestration   │
│ Fargate     → Serverless Containers     │
│ Beanstalk   → PaaS (Platform)           │
│ Batch       → Batch Computing           │
│ Lightsail   → Simple VPS                │
└─────────────────────────────────────────┘
```

### Storage Services
```
┌─────────────────────────────────────────┐
│ S3          → Object Storage            │
│ EBS         → Block Storage (EC2)       │
│ EFS         → File Storage (Linux)      │
│ FSx         → File Storage (Windows)    │
│ Glacier     → Archive Storage           │
│ Storage GW  → Hybrid Storage            │
│ Snow        → Physical Transfer         │
└─────────────────────────────────────────┘
```

### Database Services
```
┌─────────────────────────────────────────┐
│ RDS         → Relational DB             │
│ DynamoDB    → NoSQL (Key-Value)         │
│ Aurora      → High-Perf Relational      │
│ Redshift    → Data Warehouse            │
│ ElastiCache → In-Memory Cache           │
│ DocumentDB  → MongoDB-compatible        │
│ Neptune     → Graph Database            │
└─────────────────────────────────────────┘
```

### Network Services
```
┌─────────────────────────────────────────┐
│ VPC         → Virtual Network           │
│ Route 53    → DNS Service               │
│ CloudFront  → CDN                       │
│ Direct Conn → Dedicated Line            │
│ VPN         → Encrypted Connection      │
│ ALB/NLB     → Load Balancers            │
│ API Gateway → API Management            │
└─────────────────────────────────────────┘
```

---

## 🔄 Service Comparisons (Know the Difference!)

### S3 vs EBS vs EFS

```
┌─────────────┬──────────────┬──────────────┬──────────────┐
│   Feature   │      S3      │     EBS      │     EFS      │
├─────────────┼──────────────┼──────────────┼──────────────┤
│ Type        │ Object       │ Block        │ File         │
│ Access      │ HTTP/API     │ Mount        │ Mount (NFS)  │
│ Scope       │ Regional     │ AZ-specific  │ Regional     │
│ Sharing     │ Public/URL   │ Single EC2   │ Multi-EC2    │
│ Max Size    │ Unlimited    │ 64 TB/vol    │ Unlimited    │
│ Use Case    │ Static files │ Boot disk    │ Shared files │
│ Durability  │ 11 nines     │ 99.999%      │ 11 nines     │
└─────────────┴──────────────┴──────────────┴──────────────┘

REMEMBER: "Objects in S3, Blocks on EBS, Files on EFS"
```

### RDS vs DynamoDB vs Redshift

```
┌─────────────┬──────────────┬──────────────┬──────────────┐
│   Feature   │     RDS      │   DynamoDB   │   Redshift   │
├─────────────┼──────────────┼──────────────┼──────────────┤
│ Type        │ Relational   │ NoSQL        │ Data Warehouse│
│ Schema      │ Fixed        │ Flexible     │ Fixed        │
│ Scaling     │ Vertical     │ Horizontal   │ Horizontal   │
│ Query       │ SQL          │ Key-Value    │ SQL (OLAP)   │
│ Use Case    │ OLTP         │ Web apps     │ Analytics    │
│ Latency     │ Seconds      │ Milliseconds │ Seconds      │
│ Best For    │ Transactions │ High traffic │ Reports      │
└─────────────┴──────────────┴──────────────┴──────────────┘

REMEMBER: "RDS = Relations, Dynamo = Dynamic, Redshift = Reports"
```

### SQS vs SNS vs EventBridge

```
┌─────────────┬──────────────┬──────────────┬──────────────┐
│   Feature   │     SQS      │     SNS      │ EventBridge  │
├─────────────┼──────────────┼──────────────┼──────────────┤
│ Pattern     │ Queue        │ Pub/Sub      │ Event Bus    │
│ Consumers   │ 1 (pull)     │ Many (push)  │ Many (rules) │
│ Delivery    │ At least 1   │ At least 1   │ At least 1   │
│ Retention   │ Up to 14 days│ None         │ None         │
│ Order       │ FIFO option  │ No guarantee │ No guarantee │
│ Use Case    │ Decouple     │ Fan-out      │ Serverless   │
└─────────────┴──────────────┴──────────────┴──────────────┘

REMEMBER: "SQS = Stand in Queue, SNS = Send to Subscribers, EventBridge = Events Bridged"
```

---

## 🎯 One-Liner Service Definitions

### Compute
- **EC2**: Virtual servers you manage
- **Lambda**: Code that runs on events (max 15 min)
- **Fargate**: Containers without servers

### Storage
- **S3**: Infinite object storage, globally unique bucket names
- **EBS**: Hard drive for EC2 instances
- **EFS**: Network file system for multiple EC2s
- **Glacier**: Cheap archival (hours to retrieve)

### Database
- **RDS**: Managed MySQL/PostgreSQL/SQL Server/Oracle/MariaDB
- **Aurora**: AWS's fast RDS (5x MySQL, 3x PostgreSQL)
- **DynamoDB**: NoSQL for web apps (single-digit ms)
- **Redshift**: Analyze petabytes of data (data warehouse)

### Networking
- **VPC**: Your own network in AWS
- **Internet Gateway**: Connect VPC to internet
- **NAT Gateway**: Private subnet → internet (outbound only)
- **Route 53**: DNS + health checks + routing

### Security
- **IAM**: Users, groups, roles, policies
- **KMS**: Encryption key management
- **CloudTrail**: Log all API calls (audit trail)
- **GuardDuty**: Detect threats using ML

### Monitoring
- **CloudWatch**: Metrics and logs
- **CloudTrail**: API call history (who did what)
- **Config**: Track resource configuration changes

### Integration
- **SQS**: Message queue
- **SNS**: Notifications (email, SMS, push)
- **Step Functions**: Orchestrate workflows

### Analytics
- **Athena**: SQL queries on S3 (serverless)
- **Kinesis**: Real-time data streaming
- **EMR**: Hadoop/Spark clusters
- **Glue**: ETL jobs and data catalog
- **QuickSight**: BI dashboards

### Migration
- **DMS**: Migrate databases
- **DataSync**: Sync on-prem files to AWS
- **Snow**: Physical devices for massive data transfer

---

## 🧩 Pattern Recognition

### Pattern 1: "Serverless Architecture"
```
User → API Gateway → Lambda → DynamoDB
                        ↓
                       S3 (for files)
```
**Keywords**: Scalable, no servers, pay per use

### Pattern 2: "High Availability Web App"
```
Route 53 (DNS)
    ↓
CloudFront (CDN)
    ↓
ALB (Multi-AZ)
    ↓
EC2 Auto Scaling (Multi-AZ)
    ↓
RDS Multi-AZ
    ↓
S3 (static content)
```
**Keywords**: Fault-tolerant, Multi-AZ, auto-scaling

### Pattern 3: "Hybrid Cloud"
```
On-Premises ←→ Direct Connect/VPN ←→ AWS VPC
                                        ↓
                                  Storage Gateway
                                        ↓
                                       S3
```
**Keywords**: Hybrid, on-premises integration

### Pattern 4: "Data Analytics Pipeline"
```
Data Sources → Kinesis → Lambda/Analytics → S3
                                              ↓
                                           Athena
                                              ↓
                                         QuickSight
```
**Keywords**: Real-time, streaming, analytics

### Pattern 5: "Disaster Recovery"
```
Production (Region A)     Backup (Region B)
      ↓                          ↓
  RDS Multi-AZ    →→→   Read Replica (Cross-Region)
      ↓                          ↓
   S3 Bucket     →→→   S3 Cross-Region Replication
```
**Keywords**: DR, failover, cross-region

---

## 📊 Decision Trees

### Storage Decision Tree
```
Need storage?
    ├─ Object storage? → S3
    ├─ Block storage for EC2? → EBS
    ├─ Shared file system?
    │   ├─ Linux? → EFS
    │   └─ Windows? → FSx for Windows
    ├─ Archive? → Glacier
    └─ Hybrid? → Storage Gateway
```

### Database Decision Tree
```
Need database?
    ├─ Relational (SQL)?
    │   ├─ Managed? → RDS or Aurora
    │   └─ Self-managed? → EC2 + database
    ├─ NoSQL?
    │   ├─ Key-value? → DynamoDB
    │   ├─ Document? → DocumentDB
    │   └─ Graph? → Neptune
    ├─ Analytics/Warehouse? → Redshift
    └─ Cache? → ElastiCache
```

### Compute Decision Tree
```
Need compute?
    ├─ Full control? → EC2
    ├─ Event-driven? → Lambda
    ├─ Containers?
    │   ├─ Managed cluster? → ECS/EKS
    │   └─ Serverless? → Fargate
    └─ Just deploy code? → Elastic Beanstalk
```

---

## 🔢 Numbers to Remember

### S3
- **Bucket names**: 3-63 characters, globally unique
- **Object size**: 0 bytes to 5 TB
- **Single PUT**: Max 5 GB (use multi-part for larger)
- **Durability**: 99.999999999% (11 nines)
- **Availability**: 99.99% (Standard)

### EC2
- **Instance store**: Ephemeral (lost on stop/terminate)
- **EBS volume**: Max 64 TB
- **Placement groups**: 
  - Cluster = low latency
  - Spread = high availability (max 7 instances per AZ)
  - Partition = distributed apps

### Lambda
- **Max execution**: 15 minutes
- **Memory**: 128 MB to 10 GB
- **Concurrent executions**: 1,000 (default, can increase)
- **Deployment package**: 50 MB (zipped), 250 MB (unzipped)

### RDS
- **Automated backups**: 1-35 days retention
- **Max storage**: 64 TB (most engines)
- **Read replicas**: Up to 15 (Aurora), 5 (others)
- **Multi-AZ**: Automatic failover (1-2 minutes)

### DynamoDB
- **Item size**: Max 400 KB
- **Partition key**: Required (hash)
- **Sort key**: Optional (range)
- **GSI**: Max 20 per table
- **LSI**: Max 5 per table (must create with table)

### VPC
- **CIDR block**: /16 to /28
- **Subnets**: Max 200 per VPC
- **Security groups**: Max 5 per instance (default)
- **Rules per SG**: 60 inbound, 60 outbound

### CloudFront
- **Edge locations**: 400+ globally
- **TTL**: Default 24 hours (customizable)
- **Max file size**: 20 GB

---

## 🎨 Color-Coded Priority

### 🔴 MUST KNOW (High Priority)
- S3 storage classes
- EC2 instance types and purchasing options
- Security Groups vs NACLs
- IAM (users, groups, roles, policies)
- VPC basics (subnets, IGW, NAT, route tables)
- RDS Multi-AZ vs Read Replicas
- Load balancer types (ALB, NLB)
- Well-Architected Framework pillars

### 🟡 SHOULD KNOW (Medium Priority)
- Lambda limitations
- DynamoDB (tables, indexes, streams)
- Route 53 routing policies
- CloudWatch, CloudTrail, Config differences
- Auto Scaling policies
- Kinesis (Streams, Firehose, Analytics)
- EBS volume types
- S3 encryption methods

### 🟢 GOOD TO KNOW (Lower Priority)
- AWS Batch
- Step Functions
- AppSync
- Cognito
- X-Ray
- Systems Manager
- Secrets Manager
- Parameter Store

---

## 💭 Think Like AWS

### When AWS Says... They Mean...
- **"Highly available"** → Multi-AZ
- **"Fault-tolerant"** → Continue working even with failures
- **"Scalable"** → Can grow/shrink automatically
- **"Durable"** → Data won't be lost
- **"Cost-effective"** → Cheapest option that works
- **"Secure"** → Encryption, IAM, VPC
- **"Managed"** → AWS handles maintenance
- **"Serverless"** → No server management, pay per use

### AWS Prefers...
- ✅ Managed services over self-managed
- ✅ Serverless over EC2 (when possible)
- ✅ Multi-AZ over single AZ
- ✅ IAM roles over access keys
- ✅ Encryption enabled
- ✅ Least privilege access
- ✅ Auto Scaling over fixed capacity
- ✅ CloudFormation for infrastructure as code

---

## 🎬 Scenario-Based Quick Answers

### "I need to..."

**...store millions of images uploaded by users**
→ **S3** (unlimited storage, HTTP access)

**...run a MySQL database with automatic backups**
→ **RDS MySQL** with Multi-AZ

**...process data in real-time from IoT sensors**
→ **Kinesis Data Streams** → Lambda

**...send email notifications to users**
→ **SNS** (or SES for email specifically)

**...ensure my app survives AZ failure**
→ **Multi-AZ** deployment + **ALB** + **Auto Scaling**

**...analyze logs with SQL**
→ **Athena** (query S3 logs directly)

**...migrate on-prem Oracle DB to AWS**
→ **DMS** + **SCT** (Schema Conversion Tool)

**...cache database queries**
→ **ElastiCache** (Redis or Memcached)

**...store session state for web app**
→ **DynamoDB** or **ElastiCache**

**...host a static website**
→ **S3** + **CloudFront**

**...run code when file uploaded to S3**
→ **S3 Event** → **Lambda**

**...connect on-prem network to AWS securely**
→ **VPN** (quick) or **Direct Connect** (dedicated)

**...ensure compliance with data residency**
→ Choose specific **AWS Region**

**...reduce data transfer costs**
→ **CloudFront** CDN

**...implement disaster recovery**
→ **Automated backups** + **Cross-region replication**

---

## 🧪 Quick Self-Test

### Question Format: "What service should you use when..."

1. **Q**: You need to run code in response to HTTP requests without managing servers?
   **A**: API Gateway + Lambda

2. **Q**: You need a managed NoSQL database with single-digit millisecond latency?
   **A**: DynamoDB

3. **Q**: You need to distribute traffic across EC2 instances based on URL path?
   **A**: Application Load Balancer (ALB)

4. **Q**: You need to store objects up to 5 TB in size?
   **A**: S3 (use multi-part upload)

5. **Q**: You need to encrypt data at rest in S3 with your own keys?
   **A**: SSE-C (Server-Side Encryption with Customer-Provided Keys) or SSE-KMS

6. **Q**: You need to automatically scale EC2 instances based on CPU usage?
   **A**: Auto Scaling Group with target tracking policy

7. **Q**: You need to query S3 data with SQL without loading it into a database?
   **A**: Athena

8. **Q**: You need to monitor API calls made in your AWS account?
   **A**: CloudTrail

9. **Q**: You need to create a private network in AWS?
   **A**: VPC

10. **Q**: You need to transfer 100 TB of data to AWS with limited bandwidth?
    **A**: AWS Snowball

---

## 🏆 Exam Day Shortcuts

### Time-Saving Elimination Techniques

**Eliminate if the answer suggests:**
- ❌ Storing credentials in code
- ❌ Single point of failure (no redundancy)
- ❌ Opening port 22 (SSH) to 0.0.0.0/0
- ❌ Using root user for applications
- ❌ Not using encryption when security is mentioned
- ❌ Complex custom solution when AWS service exists

**Choose the answer that:**
- ✅ Uses managed AWS services
- ✅ Implements least privilege
- ✅ Has Multi-AZ/redundancy
- ✅ Uses encryption
- ✅ Is cost-effective (serverless, right-sized)
- ✅ Scales automatically

### Keywords = Services Mapping

| Keyword | Think This Service |
|---------|-------------------|
| "Real-time" | Kinesis, DynamoDB Streams |
| "Archive" | S3 Glacier |
| "Serverless" | Lambda, DynamoDB, Aurora Serverless |
| "Cache" | ElastiCache, CloudFront, DAX |
| "Queue" | SQS |
| "Notification" | SNS |
| "Workflow" | Step Functions |
| "Big Data" | EMR, Athena, Redshift |
| "Migration" | DMS, DataSync, Snow |
| "Container" | ECS, EKS, Fargate |
| "CDN" | CloudFront |
| "DNS" | Route 53 |
| "DDoS protection" | Shield, WAF |

---

## 📚 Final Memorization Tips

### The 3 P's of AWS Exam Success

1. **Patterns**: Recognize common architecture patterns
2. **Principles**: Apply Well-Architected Framework
3. **Practice**: Do practice exams

### Study Schedule Recommendation

**Week 1-2**: Core Services (EC2, S3, VPC, IAM)
**Week 3-4**: Databases & Storage (RDS, DynamoDB, EBS, EFS)
**Week 5**: Networking & Content Delivery
**Week 6**: Security & Monitoring
**Week 7**: Serverless & Application Integration
**Week 8**: Analytics, Migration, Cost Optimization
**Week 9-10**: Practice exams & review weak areas

### Memory Retention Techniques

1. **Spaced Repetition**: Review flashcards daily
2. **Active Recall**: Test yourself without looking
3. **Teach Others**: Explain concepts to someone
4. **Visual Aids**: Draw architecture diagrams
5. **Acronyms**: Use mnemonics (CROPS, SIGGIZ, etc.)
6. **Real Practice**: Use AWS Free Tier

---

**Remember**: The exam tests your ability to choose the **right** service for the **right** scenario. Focus on understanding **when** and **why** to use each service, not just **what** they do.

**You've got this! 🚀**

