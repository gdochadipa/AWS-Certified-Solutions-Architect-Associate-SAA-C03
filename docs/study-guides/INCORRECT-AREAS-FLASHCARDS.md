# 🎴 Flashcards - Incorrect Question Areas Only

## Priority Areas Based on Quiz Performance

**Focus**: Questions you got WRONG in Practice Test 1
**Total Cards**: 31 critical concepts
**Study Method**: Active recall + spaced repetition

---

## 🔴 Design Resilient Architectures (11 Cards)

### Card 1: ECS Task Definition
**Q**: What is an Amazon ECS Task Definition?

**A**: 
- **Definition**: JSON template that describes one or more containers that form your application
- **Contains**: Docker image, CPU/memory requirements, networking settings, environment variables, IAM roles, volumes
- **Purpose**: Blueprint for running containers in ECS
- **Key Point**: Task definitions are versioned and immutable

**Example Structure**:
```json
{
  "family": "my-app",
  "taskRoleArn": "arn:aws:iam::123:role/task-role",
  "containerDefinitions": [{
    "name": "app",
    "image": "myapp:v1",
    "memory": 512,
    "cpu": 256
  }]
}
```

---

### Card 2: Route 53 DNS Failover Configuration
**Q**: How do you configure Route 53 for active-passive DNS failover between AWS and on-premises?

**A**:
- **Primary**: Create Alias record for AWS resources (e.g., ALB) with "Evaluate Target Health = Yes"
- **Secondary**: Create failover record for on-premises with custom health check
- **Key Difference**: 
  - AWS resources: Use Alias + Evaluate Target Health
  - Non-AWS: Use CNAME/A record + explicit health check
- **Cannot**: Use CNAME at root domain (apex)

**Remember**: "Evaluate Target Health" works only for AWS resources!

---

### Card 3: Lambda CloudWatch Logs Permissions
**Q**: Why would Lambda function NOT write logs to CloudWatch?

**A**:
**Root Cause**: Missing IAM permissions on Lambda execution role

**Required Permissions**:
- `logs:CreateLogGroup`
- `logs:CreateLogStream`
- `logs:PutLogEvents`

**Common Mistakes**:
- ❌ Thinking CloudTrail logs Lambda output (it doesn't)
- ❌ Confusing X-Ray tracing with CloudWatch Logs
- ❌ Assuming permissions are automatic

**Fix**: Attach `AWSLambdaBasicExecutionRole` managed policy

---

### Card 4: Amazon RDS Proxy
**Q**: When should you use Amazon RDS Proxy?

**A**:
**Purpose**: Manage and pool database connections

**Use Cases**:
- High-frequency, short-lived connections (e.g., Lambda functions)
- "Too many connections" errors
- Connection storm prevention
- Idle connection management

**Benefits**:
- Reduces connection overhead
- Improves failover time (up to 66%)
- Built-in connection pooling
- Works with RDS MySQL, PostgreSQL, MariaDB, SQL Server

**Don't Use For**: Read scaling (use Read Replicas instead)

---

### Card 5: AWS Step Functions
**Q**: What is AWS Step Functions used for?

**A**:
**Purpose**: Orchestrate serverless workflows visually

**Key Features**:
- **State Machine**: Define workflow as JSON
- **Visual Workflow**: See execution in console
- **Built-in Error Handling**: Retry and catch logic
- **Service Integration**: Lambda, ECS, SNS, SQS, Glue, SageMaker

**Use Cases**:
- Multi-step Lambda workflows
- Order processing pipelines
- ETL orchestration
- Microservices coordination

**Types**:
- **Standard**: Long-running (up to 1 year)
- **Express**: High-volume, short-duration (5 min)

---

### Card 6: Route 53 Alias vs CNAME
**Q**: Can you create a CNAME record at the root domain (apex)?

**A**:
**NO!** CNAME records are NOT allowed at the zone apex (root domain).

**Solution**: Use Alias Record instead

| Feature | CNAME | Alias |
|---------|-------|-------|
| At apex (root) | ❌ Not allowed | ✅ Allowed |
| DNS query cost | Charges apply | Free |
| AWS resource | Not required | Required |
| Example | www.example.com → example.com | example.com → ALB |

**Exam Trap**: Questions showing CNAME at root domain = WRONG

**Remember**: For root domains (e.g., example.com) → Always use Alias!

---

### Card 7: Amazon SQS Cross-Account Access
**Q**: What's the best way to allow another AWS account to send messages to your SQS queue?

**A**:
**Best Practice**: Use SQS Queue Policy (resource-based policy)

**Why Not IAM Role**:
- ❌ Requires AssumeRole overhead
- ❌ More complex trust relationships
- ❌ Temporary credentials management

**Queue Policy Example**:
```json
{
  "Effect": "Allow",
  "Principal": {"AWS": "arn:aws:iam::222222:root"},
  "Action": "sqs:SendMessage",
  "Resource": "arn:aws:sqs:region:111111:my-queue"
}
```

**Key Point**: Resource-based policies are simpler and more efficient for cross-account SQS access

---

### Card 8: CloudFormation Outputs
**Q**: How do you share resources between CloudFormation stacks?

**A**:
**Use**: CloudFormation Outputs with Export/Import

**In Source Stack** (exporting):
```yaml
Outputs:
  SecurityGroupId:
    Value: !Ref MySecurityGroup
    Export:
      Name: MyApp-SecurityGroup-ID
```

**In Target Stack** (importing):
```yaml
Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      SecurityGroups:
        - !ImportValue MyApp-SecurityGroup-ID
```

**Key Points**:
- Outputs = expose values from one stack
- Export = make available for import
- ImportValue = reference in another stack
- Cannot delete exported value while in use

---

### Card 9: Amazon EKS Anywhere
**Q**: What is Amazon EKS Anywhere?

**A**:
**Purpose**: Run EKS clusters on your own infrastructure (on-premises or edge)

**Key Features**:
- Same EKS tooling as cloud
- Full Kubernetes compatibility
- Hybrid deployment support
- No internet connectivity required for cluster operation

**vs EKS Distro**:
- **EKS Anywhere**: Managed tooling + support
- **EKS Distro**: Just the open-source components

**Use Case**: Regulatory requirements, data residency, low-latency local processing

---

### Card 10: Aurora Serverless
**Q**: How does Amazon Aurora Serverless differ from provisioned Aurora?

**A**:
**Aurora Serverless**:
- ✅ Auto-scales compute capacity based on load
- ✅ Starts/stops automatically
- ✅ Pay per second
- ✅ Good for unpredictable workloads

**Aurora Provisioned**:
- ⚙️ Fixed instance size
- ⚙️ Manual scaling required
- ⚙️ Always running (pay even when idle)
- ⚙️ Good for predictable workloads

**Serverless RTO**: < 1 minute for failover

**Exam Tip**: "Variable traffic" + "no manual provisioning" = Serverless

---

### Card 11: AWS Recycle Bin
**Q**: How can you recover accidentally deleted AMIs?

**A**:
**Use**: AWS Recycle Bin for EC2

**What it Does**:
- Retains deleted EBS-backed AMIs
- User-defined retention period (1 day to 1 year)
- Simple recovery process
- No backup scripting required

**Key Points**:
- Only for EBS-backed AMIs (not instance-store)
- Must be enabled before deletion
- Free to use (storage costs apply)
- Also works for EBS snapshots

**Alternative** (more complex): Manual EBS snapshots → recreate AMI

---

## 🚀 Design High-Performing Architectures (9 Cards)

### Card 12: API Gateway Mapping Templates
**Q**: How do you transform API responses to support legacy clients in API Gateway?

**A**:
**Use**: Mapping Templates with VTL (Velocity Template Language)

**Purpose**: Transform request/response between client and backend

**Use Cases**:
- Backward compatibility
- Rename fields
- Add default values
- Restructure JSON

**Where to Configure**:
- Integration Request/Response
- Method Request/Response

**Example**:
```vtl
{
  "oldFieldName": "$input.path('$.newFieldName')"
}
```

**Not For**: Caching (API caching), error responses (Gateway responses), validation (models)

---

### Card 13: Auto Scaling Termination Policy
**Q**: Which Auto Scaling termination policy should you use to phase out instances with old AMIs?

**A**:
**Use**: `OldestLaunchTemplate`

**Purpose**: Terminates instances launched from oldest launch template version first

**Termination Policies**:
- **Default**: Balance across AZs, then oldest launch config
- **OldestInstance**: Longest-running instance
- **NewestInstance**: Most recently launched
- **OldestLaunchTemplate**: Oldest template version ⭐
- **OldestLaunchConfiguration**: Oldest launch config
- **ClosestToNextInstanceHour**: Cost optimization

**Exam Scenario**: "Update AMI across fleet" → OldestLaunchTemplate

---

### Card 14: Lambda-Backed Custom Resources
**Q**: How can you dynamically look up AMI IDs during CloudFormation stack creation?

**A**:
**Use**: AWS Lambda-backed Custom Resources in CloudFormation

**How it Works**:
1. CloudFormation calls Lambda function
2. Lambda queries EC2 for AMI ID (by tag, name, etc.)
3. Lambda returns value to CloudFormation
4. CloudFormation uses returned value in template

**Benefits**:
- Dynamic value lookup
- Custom logic during stack creation
- API integration
- DRY templates (Don't Repeat Yourself)

**Not**: SNS (notifications only), SQS (not for stack operations)

---

### Card 15: CloudFormation Mappings
**Q**: How do you select region-specific AMI IDs in CloudFormation?

**A**:
**Use**: CloudFormation Mappings + Fn::FindInMap

**Structure**:
```yaml
Mappings:
  RegionMap:
    us-east-1:
      AMI: ami-0123456789abcdef0
    eu-west-1:
      AMI: ami-0abcdef123456789
```

**Usage**:
```yaml
ImageId: !FindInMap [RegionMap, !Ref "AWS::Region", AMI]
```

**Key Points**:
- Mappings = static key-value pairs
- FindInMap = retrieves value at runtime
- Common for region-specific values (AMIs, AZs, instance types)

**Not**: Parameters (user input), Outputs (export values), Conditions (control logic)

---

### Card 16: Amazon Redshift AQUA
**Q**: How can you improve Redshift query performance without increasing cluster size?

**A**:
**Use**: AQUA (Advanced Query Accelerator) for Amazon Redshift

**What it is**:
- Hardware-accelerated cache
- Processes data closer to storage layer
- Up to 10x faster queries

**Benefits**:
- Reduces network bandwidth usage
- Offloads CPU from compute nodes
- No operational complexity
- Automatic with compatible instance types

**Use Cases**:
- Large dataset scans
- Aggregate queries
- Network/CPU bottlenecks

**Not**: Redshift Spectrum (query S3), Read Replicas (not a thing in Redshift)

---

### Card 17: AWS Application Discovery Service
**Q**: What's the best way to collect performance metrics from VMware VMs for AWS migration planning?

**A**:
**Use**: AWS Application Discovery Service - Agentless Method

**How it Works**:
- Deploy OVA appliance in VMware
- Integrates with vCenter
- Collects CPU, memory, disk, network metrics
- No agent installation on each VM

**Agent-Based Method**:
- Install Discovery Agent on each server
- More detailed application-level data
- Better for non-VMware or physical servers

**Output**: Encrypted performance data for EC2 sizing recommendations

**Exam Key**: "VMware" + "vCenter" = Agentless Discovery

---

### Card 18: EFS Cross-Region Access
**Q**: How do you access Amazon EFS from EC2 in another region and on-premises?

**A**:
**Solution**: Inter-region VPC Peering + Direct Connect

**Architecture**:
- EFS in VPC A (Region 1)
- EC2 in VPC B (Region 2)
- Inter-region VPC peering between VPC A and B
- Direct Connect to VPC B for on-premises access

**Why This Works**:
- VPC peering allows private cross-region traffic
- Direct Connect extends private network to on-premises
- All traffic stays on AWS network (not internet)

**Not**: PrivateLink (doesn't support EFS), VPN (higher latency and cost)

---

### Card 19: ElastiCache for Redis
**Q**: What's the best database service for real-time product recommendations?

**A**:
**Use**: Amazon ElastiCache for Redis

**Why**:
- Sub-millisecond latency
- In-memory key-value store
- High throughput (millions of ops/sec)
- Supports data structures (lists, sets, sorted sets)

**Use Cases**:
- Real-time personalization
- Session management
- Leaderboards
- Chat applications
- Real-time analytics

**Not Suitable**:
- Redshift (analytical, batch queries)
- Neptune (graph queries, higher latency)
- Aurora (relational, not for sub-ms latency)

---

### Card 20: Amazon Rekognition Custom Labels
**Q**: How do you identify specific animal species in camera trap images without building an ML model from scratch?

**A**:
**Use**: Amazon Rekognition Custom Labels

**How it Works**:
1. Label sample images in S3
2. Rekognition trains custom model automatically
3. Deploy model endpoint
4. Make predictions

**vs General Object Detection**:
- General: Detects "animal" broadly
- Custom Labels: Identifies specific species

**Benefits**:
- No ML expertise required
- Automatic training and deployment
- Pay only for training and inference time

**Not**: Facial Analysis (human faces only), General Rekognition (not species-specific)

---

## 🔒 Design Secure Architectures (7 Cards)

### Card 21: AWS Service Control Policies (SCPs)
**Q**: How do you prevent AWS member accounts from creating Internet Gateways?

**A**:
**Use**: Service Control Policy (SCP) in AWS Organizations

**SCP Example**:
```json
{
  "Effect": "Deny",
  "Action": [
    "ec2:CreateInternetGateway",
    "ec2:AttachInternetGateway"
  ],
  "Resource": "*"
}
```

**Key Points**:
- SCPs apply to member accounts only (NOT management account)
- Act as permission guardrails
- Don't grant permissions (only deny)
- Applied at Organization/OU/Account level

**Exam Trap**: SCPs do NOT affect the management account!

---

### Card 22: EC2 Hibernation
**Q**: How can you quickly restore a memory-intensive EC2 instance without full reinitialization?

**A**:
**Use**: EC2 Hibernation

**How it Works**:
- Saves RAM contents to EBS root volume
- Preserves instance state
- Fast resume (instance ID, IPs, volumes unchanged)

**Benefits**:
- Faster startup than stop/start
- Preserves in-memory application state
- Good for memory-intensive apps (databases, analytics)

**Limitations**:
- Max hibernate duration: 60 days
- Requires encrypted root volume
- Not all instance types supported

**Not**: AMIs (don't preserve RAM), snapshots (manual process)

---

### Card 23: Transit Gateway with ECMP
**Q**: How do you increase VPN throughput beyond 1.25 Gbps?

**A**:
**Use**: AWS Transit Gateway with ECMP (Equal-Cost Multi-Path) routing

**How it Works**:
- Create multiple Site-to-Site VPN connections
- Transit Gateway distributes traffic across all tunnels
- Enable dynamic routing (BGP)

**Benefits**:
- Aggregate throughput (multiple VPN tunnels)
- Automatic failover
- Scalable to many VPNs

**vs Virtual Private Gateway**:
- VGW: No ECMP support, single tunnel active
- TGW: ECMP enabled, parallel tunnels

**Key Point**: ECMP requires Transit Gateway + BGP

---

### Card 24: Private NAT Gateway Placement
**Q**: Where should you place a Private NAT Gateway to minimize cross-AZ data transfer costs?

**A**:
**Place**: Private NAT Gateway in the same AZ as the EC2 instances

**Cost Optimization**:
- Cross-AZ data transfer costs $0.01/GB
- Same-AZ communication: FREE
- Multiple NAT Gateways (one per AZ) reduce cross-AZ traffic

**NAT Gateway Types**:
- **Public**: Internet access, requires public subnet + EIP
- **Private**: VPC-to-VPC or on-premises access, no EIP

**Exam Scenario**: "Reduce costs" + "high traffic to internet" = NAT Gateway per AZ

---

### Card 25: AWS KMS Multi-Region Keys
**Q**: How do you reduce encryption latency for global applications?

**A**:
**Use**: AWS KMS Multi-Region Keys

**How it Works**:
- Primary key in one region
- Replicate to other regions
- Same key material across regions
- Encrypted data portable between regions

**Benefits**:
- Low-latency encryption/decryption locally
- Disaster recovery (automatic failover)
- Global data residency compliance

**Use Cases**:
- Global applications
- Multi-region databases
- Disaster recovery

**Not**: Single-region keys (cross-region latency), CloudHSM (requires management)

---

### Card 26: CloudTrail Lake
**Q**: How do you query AWS activity logs across multiple accounts and regions for compliance?

**A**:
**Use**: AWS CloudTrail Lake

**What it is**:
- Managed data lake for CloudTrail events
- SQL-based querying
- Long-term retention
- Multi-account, multi-region aggregation

**Benefits**:
- Advanced querying (not just searching)
- Compliance reporting
- No need to export to S3 + Athena
- Serverless

**vs CloudTrail Standard**:
- Standard: Log storage + basic search
- Lake: Advanced SQL queries + analysis

---

### Card 27: AWS KMS Key Types Comparison
**Q**: When should you use Asymmetric KMS Keys vs Symmetric KMS Keys?

**A**:
**Symmetric Keys** (Default):
- 256-bit AES encryption
- Same key for encrypt/decrypt
- AWS services integration (S3, EBS, RDS)
- Never leaves AWS KMS unencrypted

**Asymmetric Keys**:
- Public/private key pair (RSA or ECC)
- Digital signatures and verification
- Public key encryption (offline)
- Use cases: Code signing, JWT tokens

**Quick Decision**:
- Encryption/decryption in AWS: **Symmetric**
- Digital signatures: **Asymmetric**
- Public key distribution: **Asymmetric**

---

## 💰 Design Cost-Optimized Architectures (4 Cards)

### Card 28: AWS Resource Access Manager (RAM)
**Q**: How do you share resources across AWS accounts without duplication?

**A**:
**Use**: AWS Resource Access Manager (RAM)

**What You Can Share**:
- VPC subnets
- Transit Gateway attachments
- Route 53 Resolver rules
- License configurations
- Resource Groups

**Benefits**:
- No resource duplication
- Centralized governance
- Consistent billing
- Works within AWS Organizations

**Exam Scenario**: "Multiple accounts" + "duplicate resources" + "cost reduction" = RAM

---

### Card 29: NAT Gateway Cost Optimization
**Q**: What's the most cost-effective NAT Gateway configuration for high-traffic workloads?

**A**:
**Best Practice**: One Public NAT Gateway per AZ with high-traffic instances

**Cost Factors**:
- **NAT Gateway hourly charge**: $0.045/hour
- **Data processing**: $0.045/GB
- **Cross-AZ data transfer**: $0.01/GB

**Optimization**:
- Place NAT Gateway in same AZ as instances (avoid cross-AZ)
- Use one NAT Gateway per AZ (not multiple per AZ)
- Consider NAT Instances for very low traffic (but less reliable)

**Don't**: Use Private NAT Gateway for internet access (it can't do that!)

---

### Card 30: Cost Allocation Tags in AWS Organizations
**Q**: How can the management account view NAT Gateway costs across all member accounts?

**A**:
**Use**: Cost Allocation Tags activated by management account

**Process**:
1. Member accounts tag their NAT Gateways
2. Management account activates tags in Cost Allocation Tags manager
3. View detailed costs in Cost Explorer or billing reports

**Key Points**:
- Tags must be applied in resource-owning account
- Management account activates tags organization-wide
- Only management account sees consolidated billing
- Member accounts can't see full organization costs

**Exam Tip**: "Combined view across accounts" = Management account + Cost Allocation Tags

---

### Card 31: AWS Application Migration Service
**Q**: What's the best service to migrate on-premises SQL Server to AWS with minimal downtime?

**A**:
**Use**: AWS Application Migration Service (formerly CloudEndure)

**How it Works**:
- Continuous replication of source servers
- Automated server conversion
- Pre-cutover testing
- Minimal downtime cutover

**Benefits**:
- Lift-and-shift migration
- No application changes required
- Automated failover
- Works with physical, virtual, and cloud servers

**vs Other Services**:
- Migration Hub: Tracking only
- DataSync: File/object storage only
- Database Migration Service: Databases only (not full servers)

---

## 🎯 Study Strategy

### Daily Review Schedule:
- **Morning**: 5 cards (active recall)
- **Afternoon**: 5 cards (write answers)
- **Evening**: 5 cards (teach someone else)

### Spaced Repetition:
- Day 1: Learn cards 1-10
- Day 2: Review cards 1-10 + Learn cards 11-20
- Day 3: Review cards 1-10 + Learn cards 21-31
- Day 4: Review all 31 cards
- Day 7: Review all 31 cards
- Day 14: Review all 31 cards

### Active Recall Technique:
1. Read question
2. Answer WITHOUT looking
3. Check answer
4. Mark if correct/incorrect
5. Focus on incorrect cards

---

**Remember**: These 31 cards cover ONLY the questions you got wrong. Master these, and you'll significantly improve your score!

**Next Step**: Take section quizzes to reinforce these concepts in different scenarios.

