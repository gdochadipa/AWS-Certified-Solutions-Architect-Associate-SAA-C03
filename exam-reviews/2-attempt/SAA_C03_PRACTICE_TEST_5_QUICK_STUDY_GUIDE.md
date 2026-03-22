# AWS SAA-C03 Quick Study Guide - Practice Test 5 Review
## Focus Areas for 2nd → 3rd Attempt

---

## 🚨 CRITICAL: High-Performing Architectures

### ECS Deployment & Networking

#### ECS Launch Types
```
┌─────────────────────────────────────────┐
│         ECS Launch Types                │
├─────────────────────────────────────────┤
│ EC2 Launch Type                         │
│ ├── Control over instances             │
│ ├── Pick instance family/size          │
│ ├── Persistent storage options         │
│ └── ✅ Standard for AWS Outposts       │
│                                         │
│ Fargate Launch Type                    │
│ ├── Serverless container compute       │
│ ├── No instance management             │
│ └── ❌ Limited Outposts support        │
└─────────────────────────────────────────┘
```

#### ECS Networking Modes (EC2)
```
┌──────────────────────────────────────────────────────┐
│ Host Mode                                            │
│ ├── Container shares host network namespace         │
│ ├── Port conflicts possible                         │
│ └── ❌ No task-level security groups                │
├──────────────────────────────────────────────────────┤
│ Bridge Mode (default)                               │
│ ├── Docker bridge network                           │
│ ├── Port mapping (container:host)                   │
│ └── ❌ No per-task ENI or security groups          │
├──────────────────────────────────────────────────────┤
│ awsvpc Mode ⭐                                       │
│ ├── Each task gets own ENI                          │
│ ├── Task-level security groups                      │
│ ├── VPC Flow Logs per task                          │
│ └── ✅ Required for task-level network controls     │
└──────────────────────────────────────────────────────┘
```

#### ECS Dynamic Port Mapping
```
Requirement: Multiple tasks per instance

┌────────────────────────────────────┐
│ Load Balancer Support              │
├────────────────────────────────────┤
│ ✅ Application Load Balancer       │
│    └── HTTP/HTTPS, Layer 7         │
│                                    │
│ ✅ Network Load Balancer           │
│    └── TCP/UDP, Layer 4            │
│                                    │
│ ❌ Classic Load Balancer           │
│    └── No dynamic port support     │
└────────────────────────────────────┘

Configuration:
- Container port: 80 (fixed)
- Host port: 0 (ephemeral range)
- Target group registers dynamic ports automatically
```

---

### Load Balancer Deep Dive

#### ALB Routing Types
```
┌───────────────────────────────────────────────────┐
│ HOST-BASED ROUTING                                │
│ ├── Routes based on Host header                  │
│ ├── Example: api.example.com vs www.example.com  │
│ └── Use case: Different domains/subdomains       │
├───────────────────────────────────────────────────┤
│ PATH-BASED ROUTING                                │
│ ├── Routes based on URL path                     │
│ ├── Example: /api/* vs /images/*                 │
│ └── Use case: Microservices on same domain       │
├───────────────────────────────────────────────────┤
│ QUERY STRING/HEADER ROUTING                       │
│ ├── Routes based on query params or headers      │
│ ├── Example: ?version=v2                         │
│ └── Use case: A/B testing, API versioning        │
└───────────────────────────────────────────────────┘
```

#### ALB vs NLB Comparison
```
┌──────────────────────┬──────────────┬──────────────┐
│ Feature              │ ALB          │ NLB          │
├──────────────────────┼──────────────┼──────────────┤
│ OSI Layer            │ 7 (HTTP)     │ 4 (TCP/UDP)  │
│ Static IP            │ ❌           │ ✅           │
│ Elastic IP           │ ❌           │ ✅           │
│ Host-based routing   │ ✅           │ ❌           │
│ Path-based routing   │ ✅           │ ❌           │
│ WebSocket            │ ✅           │ ✅           │
│ Dynamic port mapping │ ✅           │ ✅           │
│ Ultra-low latency    │ Good         │ Best         │
│ TLS termination      │ ✅           │ ✅           │
│ Preserve source IP   │ Via header   │ Native       │
└──────────────────────┴──────────────┴──────────────┘
```

---

### S3 Performance Optimization

#### Write Performance (80% bottleneck)
```
┌─────────────────────────────────────────────┐
│ SOLUTION: Multipart + Parallelization      │
├─────────────────────────────────────────────┤
│ 1. Multipart Upload                         │
│    ├── Break large objects into parts       │
│    ├── 5MB - 5GB per part (max 10,000)     │
│    ├── Parallel upload of parts             │
│    └── Automatic retry on part failure      │
│                                             │
│ 2. Parallelization                          │
│    ├── Multiple concurrent PUT requests     │
│    ├── Distribute across prefixes           │
│    └── 3,500 PUT/COPY/POST per prefix/sec  │
│                                             │
│ 3. Transfer Acceleration                    │
│    ├── Upload to nearest edge location      │
│    ├── AWS backbone to bucket region        │
│    └── Best for global uploads              │
│                                             │
│ 4. Prefix Design                            │
│    ├── Avoid hot prefixes                   │
│    ├── Hash/random prefix distribution      │
│    └── Example: /a7/b3/object vs /static/   │
└─────────────────────────────────────────────┘
```

#### Read Performance & LIST Operations (20% bottleneck)
```
❌ WRONG: Scale LIST operations
   └── More LIST calls = more overhead
   └── Doesn't solve root problem

✅ RIGHT: Build Catalog Index

┌─────────────────────────────────────────┐
│ Option 1: DynamoDB Catalog              │
│ ├── Key: object_id or path             │
│ ├── Attributes: metadata, location     │
│ ├── Update via S3 Event Notifications  │
│ └── Query instead of LIST               │
├─────────────────────────────────────────┤
│ Option 2: S3 Inventory + Athena        │
│ ├── Daily/weekly inventory to S3       │
│ ├── Query with Athena (serverless SQL) │
│ └── Best for batch analytics            │
├─────────────────────────────────────────┤
│ Option 3: OpenSearch Service           │
│ ├── Real-time indexing via Lambda      │
│ ├── Full-text search capabilities      │
│ └── Complex query support               │
└─────────────────────────────────────────┘
```

---

### CloudFront Architecture

#### Custom Error Pages
```
┌──────────────────────────────────────────────┐
│ STEP-BY-STEP CONFIGURATION                   │
├──────────────────────────────────────────────┤
│ 1. Store Error Pages in S3                   │
│    ├── Create S3 bucket (e.g., errors-cdn)  │
│    ├── Upload 500.html, 502.html, etc.      │
│    └── Set up OAC/OAI (keep private)        │
│                                              │
│ 2. Configure Custom Error Responses          │
│    ├── Go to CloudFront distribution         │
│    ├── Error Pages tab                       │
│    ├── Create Custom Error Response          │
│    │   ├── HTTP Error Code: 500             │
│    │   ├── Response Page Path: /500.html    │
│    │   ├── HTTP Response Code: 500 or 200   │
│    │   └── Error Caching Min TTL: 300       │
│    └── Repeat for 502, 503, 504, etc.       │
│                                              │
│ 3. Create Cache Behavior (if needed)         │
│    ├── Path pattern: /errors/*               │
│    ├── Origin: S3 error pages bucket         │
│    └── Cache policy: CachingOptimized       │
└──────────────────────────────────────────────┘

⚠️ COMMON MISTAKE:
"Upload error pages directly to CloudFront"
└── CloudFront is CDN, not storage!
    All content must be at an origin (S3/HTTP)
```

---

### Global Accelerator vs Route 53

#### When to Use Each
```
┌────────────────────────────────────────────────┐
│ AWS GLOBAL ACCELERATOR ⭐                      │
├────────────────────────────────────────────────┤
│ Provides:                                      │
│ ├── 2 static anycast IPv4 addresses           │
│ ├── Traffic on AWS global network             │
│ ├── Health-based automatic failover           │
│ └── Instant regional failover                 │
│                                                │
│ Use when you need:                             │
│ ├── Static IPs (avoid DNS caching)            │
│ ├── Fast regional failover (instant)          │
│ ├── Non-HTTP protocols                        │
│ ├── Deterministic routing                     │
│ └── IoT/gaming/VoIP applications              │
└────────────────────────────────────────────────┘

┌────────────────────────────────────────────────┐
│ AMAZON ROUTE 53                                │
├────────────────────────────────────────────────┤
│ Provides:                                      │
│ ├── DNS-based routing                         │
│ ├── Multiple routing policies                 │
│ ├── Health checks                             │
│ └── Domain registration                       │
│                                                │
│ Use when you need:                             │
│ ├── DNS management                            │
│ ├── Multiple routing policies                 │
│ ├── Cost optimization (cheaper)               │
│ ├── HTTP/HTTPS only                           │
│ └── Standard web applications                 │
│                                                │
│ ⚠️ Does NOT provide:                          │
│ └── Static anycast IPs                        │
│ └── PrivateLink endpoint (doesn't exist!)    │
└────────────────────────────────────────────────┘
```

---

### Auto Scaling Best Practices

#### Scaling Policy Comparison
```
┌─────────────────────────────────────────────────┐
│ SIMPLE SCALING ❌                               │
│ ├── Fixed adjustment (e.g., +1 instance)       │
│ ├── Cooldown period after each action          │
│ └── Can oscillate/slow to respond              │
├─────────────────────────────────────────────────┤
│ STEP SCALING                                    │
│ ├── Multiple steps based on metric value       │
│ ├── Faster than simple scaling                 │
│ └── Still reactive to current state            │
├─────────────────────────────────────────────────┤
│ TARGET TRACKING ⭐ (RECOMMENDED)                │
│ ├── Specify target metric value                │
│ ├── ASG adjusts to maintain target             │
│ ├── Handles both scale-out and scale-in        │
│ └── Works well with AZ rebalancing             │
├─────────────────────────────────────────────────┤
│ PREDICTIVE SCALING                              │
│ ├── ML-based forecasting                       │
│ ├── Schedules capacity before load             │
│ └── Adds complexity and cost                   │
└─────────────────────────────────────────────────┘
```

#### AZ Rebalancing
```
Problem: Hot spot in one AZ after scaling

┌──────────────────────────────────────────┐
│ SOLUTION: Target Tracking + AZ Rebalance│
├──────────────────────────────────────────┤
│ 1. Configure Target Tracking Policy      │
│    ├── Metric: Average CPU utilization   │
│    ├── Target: 50%                       │
│    └── ASG adjusts capacity to target    │
│                                          │
│ 2. Enable AZ Rebalancing                 │
│    ├── Default: enabled                  │
│    ├── Redistributes instances evenly    │
│    └── No additional scaling cost        │
│                                          │
│ 3. Results                               │
│    ├── Balanced AZ distribution          │
│    ├── No hot spots                      │
│    └── Maintains target metric           │
└──────────────────────────────────────────┘
```

---

### EC2 Networking

#### Stop/Start Behavior
```
┌─────────────────────────────────────────────┐
│ EBS-BACKED INSTANCES                        │
├─────────────────────────────────────────────┤
│ Can be: STOPPED and STARTED ✅              │
│                                             │
│ On STOP:                                    │
│ ├── Private IP: PRESERVED                  │
│ ├── Public IP: RELEASED                    │
│ ├── EBS volumes: PRESERVED                 │
│ └── Instance may move to different host    │
│                                             │
│ On START:                                   │
│ ├── Private IP: SAME                       │
│ ├── Public IP: NEW (unless EIP attached)   │
│ ├── Security Groups: PRESERVED             │
│ └── IAM Role: PRESERVED                    │
└─────────────────────────────────────────────┘

🔧 FIX for SSH Issues:
   1. Use Elastic IP (static public IP)
   2. Or use private IP via VPN/DirectConnect
   3. Or update SSH config with new public IP
```

---

## ⚠️ IMPORTANT: Secure Architectures

### RDS Scaling Patterns

#### Multi-AZ vs Read Replicas
```
┌─────────────────────────────────────────────┐
│ MULTI-AZ ❌ FOR READ SCALING                │
├─────────────────────────────────────────────┤
│ Purpose: High Availability                  │
│ ├── Synchronous replication                │
│ ├── Automatic failover                      │
│ ├── Same region, different AZ              │
│ └── Standby NOT accessible for reads       │
│                                             │
│ Use for:                                    │
│ ├── Disaster recovery                       │
│ ├── Maintenance windows                     │
│ └── AZ failure protection                   │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ READ REPLICAS ✅ FOR READ SCALING           │
├─────────────────────────────────────────────┤
│ Purpose: Read Performance                   │
│ ├── Asynchronous replication               │
│ ├── Can be in different region             │
│ ├── Up to 5 read replicas                  │
│ └── Each replica can have own replicas     │
│                                             │
│ Use for:                                    │
│ ├── Read-heavy workloads                   │
│ ├── Reporting queries                       │
│ ├── Analytics workloads                     │
│ └── Geographic distribution                 │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ ELASTICACHE ⭐ BEST FOR READ-HEAVY          │
├─────────────────────────────────────────────┤
│ Purpose: Extreme Read Performance           │
│ ├── In-memory data store                   │
│ ├── Sub-millisecond latency                │
│ ├── Redis or Memcached                     │
│ └── Removes load from database             │
│                                             │
│ Use for:                                    │
│ ├── Session stores                         │
│ ├── Frequently accessed data               │
│ ├── Real-time analytics                    │
│ └── Leaderboards, counters                │
└─────────────────────────────────────────────┘
```

---

### IAM Access Patterns

#### S3 Bucket Access Control
```
❌ AVOID: Explicit Deny Lists
┌────────────────────────────────────────┐
│ Bucket Policy:                         │
│ {                                      │
│   "Effect": "Deny",                    │
│   "Principal": "*",                    │
│   "Action": "s3:*",                    │
│   "Condition": {                       │
│     "StringNotEquals": {               │
│       "aws:userid": [                  │
│         "user1-id",                    │
│         "user2-id",                    │
│         "user3-id"  ← Hard to maintain│
│       ]                                │
│     }                                  │
│   }                                    │
│ }                                      │
└────────────────────────────────────────┘

✅ PREFER: Role-Based Access
┌────────────────────────────────────────┐
│ Bucket Policy:                         │
│ {                                      │
│   "Effect": "Allow",                   │
│   "Principal": {                       │
│     "AWS": "arn:aws:iam::ACCT:role/HR" │
│   },                                   │
│   "Action": "s3:*",                    │
│   "Resource": [                        │
│     "arn:aws:s3:::hr-bucket/*"         │
│   ]                                    │
│ }                                      │
│                                        │
│ Users: Assume HR role to access       │
│ ├── Can add MFA requirement           │
│ ├── Centralized management            │
│ └── Easy to add/remove users          │
└────────────────────────────────────────┘
```

---

### Network Security

#### Security Groups vs Network ACLs
```
┌────────────────────────────────────────────────┐
│ SECURITY GROUPS (Instance-level)               │
├────────────────────────────────────────────────┤
│ Stateful: Return traffic automatically allowed │
│ Rules: ALLOW only (no DENY)                    │
│ Evaluation: All rules evaluated                │
│                                                │
│ Use for:                                       │
│ ├── Instance-level security                   │
│ ├── Application-specific rules                │
│ └── Dynamic IP groups                         │
│                                                │
│ ❌ Cannot:                                     │
│ └── Explicitly DENY traffic                   │
│ └── Block specific IPs at subnet level        │
└────────────────────────────────────────────────┘

┌────────────────────────────────────────────────┐
│ NETWORK ACLs (Subnet-level) ⭐ for DoS         │
├────────────────────────────────────────────────┤
│ Stateless: Must allow return traffic           │
│ Rules: ALLOW and DENY                          │
│ Evaluation: In order by rule number            │
│                                                │
│ Use for:                                       │
│ ├── Subnet-level security                     │
│ ├── DoS/DDoS protection                       │
│ ├── Block IP ranges                           │
│ └── Compliance requirements                   │
│                                                │
│ ✅ Can:                                        │
│ ├── Explicitly DENY traffic                   │
│ └── Block before reaching instances           │
└────────────────────────────────────────────────┘

Example DoS Protection:
Rule # | Type   | Protocol | Port | Source      | Allow/Deny
-------|--------|----------|------|-------------|------------
100    | Inbound| TCP      | 3306 | 0.0.0.0/0  | DENY
*      | Inbound| ALL      | ALL  | 0.0.0.0/0  | ALLOW
```

---

### Secrets Management

#### Secrets Manager vs Parameter Store
```
┌─────────────────────────────────────────────┐
│ SECRETS MANAGER ⭐                          │
├─────────────────────────────────────────────┤
│ Features:                                   │
│ ├── Automatic rotation                     │
│ ├── Built-in rotation for RDS/Aurora       │
│ ├── Custom rotation Lambda                 │
│ ├── Fine-grained IAM                       │
│ └── Encryption at rest (KMS)               │
│                                             │
│ Built-in Rotation:                          │
│ ├── RDS (MySQL, PostgreSQL, etc.)          │
│ ├── DocumentDB                             │
│ └── Redshift                               │
│                                             │
│ Custom Rotation:                            │
│ ├── API keys                               │
│ ├── OAuth tokens                           │
│ ├── 3rd party services                     │
│ └── Lambda function required               │
│                                             │
│ Cost: ~$0.40/secret/month + $0.05/10K API  │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ PARAMETER STORE                             │
├─────────────────────────────────────────────┤
│ Features:                                   │
│ ├── NO automatic rotation                  │
│ ├── Hierarchical storage                   │
│ ├── Standard tier: Free                    │
│ ├── Advanced tier: $0.05/parameter         │
│ └── Integration with SSM                   │
│                                             │
│ Use for:                                    │
│ ├── Configuration data                     │
│ ├── Non-rotating secrets                   │
│ └── Cost-sensitive applications            │
│                                             │
│ ❌ Does NOT support:                        │
│ └── Automatic credential rotation          │
└─────────────────────────────────────────────┘
```

#### Custom Rotation Lambda Pattern
```python
# Secrets Manager Rotation Lambda Structure

def lambda_handler(event, context):
    """
    Step 1: createSecret
    - Generate new password/key
    - Store as AWSPENDING version
    """
    
    """
    Step 2: setSecret
    - Update service with new credential
    - Test that new credential works
    """
    
    """
    Step 3: testSecret
    - Verify new credential is functional
    - Can connect/authenticate with it
    """
    
    """
    Step 4: finishSecret
    - Mark AWSPENDING as AWSCURRENT
    - Old credential becomes AWSPREVIOUS
    """
    
    # Implementation varies by service type
```

---

### AWS Monitoring Services

#### CloudTrail vs Config vs CloudWatch
```
┌─────────────────────────────────────────────┐
│ CLOUDTRAIL ⭐ for "Who did what?"           │
├─────────────────────────────────────────────┤
│ Tracks:                                     │
│ ├── API calls (management events)          │
│ ├── Who, when, from where                  │
│ ├── Success/failure status                 │
│ └── Request/response details               │
│                                             │
│ Use for:                                    │
│ ├── Security auditing                      │
│ ├── Compliance                             │
│ ├── Organization-wide logging              │
│ └── Incident investigation                 │
│                                             │
│ Organization Features:                      │
│ ├── Single trail for all accounts          │
│ ├── Cross-account collection               │
│ └── Centralized S3 bucket                  │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ AWS CONFIG - "What changed?"                │
├─────────────────────────────────────────────┤
│ Tracks:                                     │
│ ├── Resource configuration changes         │
│ ├── Relationships between resources        │
│ ├── Compliance against rules               │
│ └── Configuration timeline                 │
│                                             │
│ Use for:                                    │
│ ├── Configuration compliance               │
│ ├── Resource inventory                     │
│ ├── Change management                      │
│ └── Security analysis                      │
│                                             │
│ ❌ NOT for:                                 │
│ └── API call logging                       │
│ └── Administrator activity                 │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ CLOUDWATCH - "How is it performing?"       │
├─────────────────────────────────────────────┤
│ Tracks:                                     │
│ ├── Metrics (CPU, network, custom)         │
│ ├── Logs (application, system)             │
│ ├── Alarms and notifications               │
│ └── Dashboards                             │
│                                             │
│ Use for:                                    │
│ ├── Performance monitoring                 │
│ ├── Operational health                     │
│ ├── Alerting                               │
│ └── Troubleshooting                        │
└─────────────────────────────────────────────┘
```

---

### Storage Gateway

#### Gateway Type Selection
```
┌─────────────────────────────────────────────┐
│ FILE GATEWAY ⭐                             │
├─────────────────────────────────────────────┤
│ Protocol: SMB, NFS                          │
│ Backend: S3 bucket (as objects)             │
│ Use case:                                   │
│ ├── File share on-premises                 │
│ ├── Data stored as S3 objects              │
│ ├── Admin needs S3 console access          │
│ └── Cloud backup/archival                  │
│                                             │
│ ✅ Admins can:                              │
│ ├── Browse objects in S3 console           │
│ ├── Use S3 APIs directly                   │
│ └── Set S3 lifecycle policies              │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ VOLUME GATEWAY (Cached/Stored)             │
├─────────────────────────────────────────────┤
│ Protocol: iSCSI (block storage)             │
│ Backend: EBS snapshots in S3                │
│ Use case:                                   │
│ ├── Block storage for apps                 │
│ ├── Disaster recovery                      │
│ └── Migration to AWS                       │
│                                             │
│ ❌ Data NOT accessible as:                  │
│ └── Normal S3 objects in console           │
│ └── Must restore from snapshot             │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ TAPE GATEWAY                                │
├─────────────────────────────────────────────┤
│ Protocol: iSCSI VTL                         │
│ Backend: S3 Glacier/Deep Archive            │
│ Use case:                                   │
│ ├── Backup applications                    │
│ ├── Tape library replacement               │
│ └── Long-term archival                     │
│                                             │
│ ❌ NOT for:                                 │
│ └── Operational file storage               │
│ └── Real-time object access                │
└─────────────────────────────────────────────┘
```

---

## 🎯 Quick Decision Trees

### "Which load balancer?"
```
Need Layer 7 features?
├── YES → Application Load Balancer
│   ├── Host/path routing
│   ├── HTTP/HTTPS/WebSocket
│   └── Lambda targets
└── NO
    ├── Need static IP? → Network Load Balancer
    │   ├── Extreme performance
    │   ├── TCP/UDP/TLS
    │   └── Preserve source IP
    └── Legacy app? → Classic Load Balancer (deprecate!)
```

### "How to scale reads?"
```
Read-heavy database?
├── Hot data cached? → ElastiCache (best)
├── Cross-region reads? → Read Replicas
├── Analytics queries? → Read Replicas
└── Just HA? → Multi-AZ (not for reads!)
```

### "Network security?"
```
Need to DENY traffic?
├── Instance-level? → Security Group (can't deny!)
└── Subnet-level? → Network ACL ✅

Facing DoS attack?
└── Network ACL with DENY rules
```

### "Secrets rotation?"
```
Need automatic rotation?
├── YES
│   ├── RDS/Aurora? → Secrets Manager (built-in)
│   └── API keys? → Secrets Manager (custom Lambda)
└── NO
    └── Static config? → Parameter Store (free)
```

---

## 🔄 Common Mistake Patterns

### Mistake #1: Confusing HA with Read Scaling
```
❌ Multi-AZ is for reads
✅ Multi-AZ is for availability only
   Read Replicas are for read scaling
   ElastiCache is BEST for read-heavy
```

### Mistake #2: Storage Gateway Confusion
```
❌ "Tape Gateway for file storage"
✅ File Gateway = Files as S3 objects
   Volume Gateway = Block storage/snapshots
   Tape Gateway = VTL/archive only
```

### Mistake #3: Security Group Capabilities
```
❌ "Use Security Group to DENY IP"
✅ Security Groups can't DENY
   Use Network ACL for explicit DENY
```

### Mistake #4: CloudFront Storage
```
❌ "Upload content directly to CloudFront"
✅ CloudFront is CDN, not storage
   Content must be at origin (S3/HTTP)
```

### Mistake #5: ECS Launch Types
```
❌ "Fargate on Outposts for standard workloads"
✅ EC2 launch type is standard for Outposts
   Fargate on Outposts is limited
```

---

## 📚 Must-Memorize Facts

### ECS
- awsvpc = task-level ENI + security groups
- Dynamic port mapping = ALB or NLB (not CLB)
- Outposts = EC2 launch type (Fargate limited)

### Load Balancers
- ALB = Layer 7, host/path routing, no static IP
- NLB = Layer 4, static IP/EIP, ultra-low latency
- Dynamic ports = ALB + NLB ✅, CLB ❌

### S3 Performance
- Write bottleneck = Multipart + Parallelization
- LIST bottleneck = Catalog index (DynamoDB/OpenSearch)
- DON'T scale LIST calls (makes worse)

### CloudFront
- Custom Error Responses = S3 origin with error pages
- Can't upload directly to CloudFront
- Must use origin (S3 or HTTP)

### Global Accelerator
- Provides 2 static anycast IPs
- Traffic on AWS backbone
- Use for IoT, gaming, static IP needs
- Route 53 does NOT provide static IPs

### Auto Scaling
- Target tracking = best for AZ rebalancing
- AZ rebalancing = no extra cost
- Simple scaling = can oscillate

### RDS
- Multi-AZ = HA only (standby not for reads)
- Read Replicas = read scaling
- ElastiCache = BEST for read-heavy

### Security
- Security Groups = allow only (no deny)
- Network ACL = allow + DENY (use for DoS)
- Secrets Manager = rotation ✅
- Parameter Store = NO rotation ❌

### Monitoring
- CloudTrail = API calls (who did what)
- Config = configuration changes (what changed)
- CloudWatch = performance (how is it running)

### Storage Gateway
- File Gateway = S3 objects (SMB/NFS)
- Volume Gateway = EBS snapshots (iSCSI)
- Tape Gateway = VTL archive

---

## ⚡ Last-Minute Checklist

Before next attempt, ensure you can answer:

- [ ] Which ECS networking mode gives task-level security groups?
- [ ] Which load balancers support dynamic port mapping?
- [ ] How to optimize S3 LIST operations at scale?
- [ ] Where do CloudFront error pages actually live?
- [ ] What does Global Accelerator provide that Route 53 doesn't?
- [ ] Which Auto Scaling policy works best with AZ rebalancing?
- [ ] What happens to EC2 public IP on stop/start?
- [ ] Can Multi-AZ standby be used for read traffic?
- [ ] Which AWS service records administrator API calls?
- [ ] Can Security Groups explicitly DENY traffic?
- [ ] Does Secrets Manager support automatic rotation?
- [ ] Which Storage Gateway type stores files as S3 objects?

If you can't immediately answer these, review the relevant sections above!

---

**Study Time Estimate:** 10-12 hours to master these concepts  
**Recommended Practice:** 2 more practice tests focusing on these areas  
**Target Score:** 80%+ on next attempt

Good luck! 🚀

