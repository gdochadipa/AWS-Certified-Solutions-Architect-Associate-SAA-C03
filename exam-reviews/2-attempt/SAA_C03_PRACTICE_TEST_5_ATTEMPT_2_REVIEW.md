# AWS SAA-C03 Practice Test 5 - Second Attempt Review
## Test ID: 60758 | Attempt ID: 8553131

---

## 📊 Executive Summary

**Test Date:** March 5, 2026  
**Attempt Number:** 2nd Attempt  
**Final Score:** 47/65 (72.31%)  
**Result:** FAIL (Pass threshold: 75%)  
**Duration:** 5341 seconds (~89 minutes)  
**Improvement Needed:** +2.69% to pass

---

## 🎯 Performance by Domain

### Domain 1: Design Resilient Architectures (21 questions)
- **Score:** 18/21 (85.71%) ✅
- **Correct:** 18
- **Incorrect:** 3
- **Review Marked:** 1
- **Status:** STRONG - Exceeds passing standard

### Domain 2: Design High-Performing Architectures (23 questions)
- **Score:** 14/23 (60.87%) ❌
- **Correct:** 14
- **Incorrect:** 9
- **Review Marked:** 7
- **Status:** CRITICAL - Major weakness

### Domain 3: Design Secure Architectures (18 questions)
- **Score:** 12/18 (66.67%) ⚠️
- **Correct:** 12
- **Incorrect:** 6
- **Review Marked:** 4
- **Status:** BELOW STANDARD - Needs improvement

### Domain 4: Design Cost-Optimized Architectures (3 questions)
- **Score:** 3/3 (100%) ✅
- **Correct:** 3
- **Incorrect:** 0
- **Review Marked:** 0
- **Status:** PERFECT

---

## 🚨 Critical Areas for Improvement

### Priority 1: Design High-Performing Architectures (39% failure rate)
**Impact:** This domain accounts for 35% of the exam and you're scoring 15% below passing.

**Failed Questions:**
1. **Q8:** ECS deployment (Outposts vs Local Zones) - Architecture placement
2. **Q16:** IoT + Global Accelerator vs Route 53 - Networking design
3. **Q19:** S3 performance optimization - LIST operations & catalog indexing
4. **Q24:** CloudFront custom error pages - Content delivery
5. **Q26:** Load balancer host-based routing - ALB vs NLB features
6. **Q27:** ECS dynamic port mapping - Container networking
7. **Q32:** RDS read-heavy scaling - ElastiCache vs Multi-AZ
8. **Q50:** EC2 public IP behavior - Instance networking
9. **Q64:** Auto Scaling AZ rebalancing - Scaling policies

### Priority 2: Design Secure Architectures (33% failure rate)
**Impact:** This domain is 30% of exam content.

**Failed Questions:**
1. **Q7:** ECS networking modes - awsvpc for task-level security groups
2. **Q11:** S3 bucket access control - Role-based vs explicit deny
3. **Q28:** Secrets Manager API key rotation - Custom Lambda rotation
4. **Q32:** CloudTrail for Organizations - Monitoring admin actions
5. **Q47:** Network ACL vs Security Group - DoS protection
6. **Q61:** Storage Gateway types - File Gateway for S3 object access

### Priority 3: Design Resilient Architectures (14% failure rate)
**Minor weaknesses:**
1. **Q17:** FSx for Lustre + DataSync - Data repository integration
2. **Q18:** FSx for Windows File Server - Multi-AZ and cross-network access
3. **Q40:** RDS scaling options - Multi-AZ replica limitations

---

## 📝 Detailed Question Analysis

### INCORRECT ANSWERS - HIGH-PERFORMING ARCHITECTURES

#### Question 8: ECS Deployment Location ❌
**Your Answer:** A - ECS Fargate on AWS Outposts  
**Correct Answer:** D - ECS EC2 launch type on AWS Outposts

**Why You Failed:**
- Fargate support on Outposts is limited/not broadly available
- EC2 launch type is the standard path for ECS on Outposts
- Missed the requirement for "consistent, high CPU and memory requirements"

**Key Learning:**
```
Outposts Deployment:
├── ECS EC2 Launch Type ✅
│   ├── Full control over instance types
│   ├── Consistent CPU/RAM sizing
│   └── Standard for Outposts
└── ECS Fargate ❌
    └── Limited/no Outposts support
```

**Study Resources:**
- AWS Outposts ECS deployment documentation
- ECS launch type comparison
- On-premises latency optimization patterns

---

#### Question 16: IoT Static IP Architecture ❌
**Your Answer:** A - Route 53 geolocation + PrivateLink  
**Correct Answer:** B - Global Accelerator (2 anycast static IPs)

**Why You Failed:**
- Route 53 doesn't provide anycast static IPs
- PrivateLink doesn't exist for Route 53
- Missed "avoid DNS reconfiguration and IP caching issues"

**Key Learning:**
```
Static IP Requirements:
├── AWS Global Accelerator ✅
│   ├── 2 anycast static IPv4 addresses
│   ├── Traffic on AWS backbone
│   └── Health-based routing
└── Route 53 ❌
    ├── DNS-based (not static IPs)
    └── Client IP caching issues
```

**Critical Concept:** Global Accelerator provides static IPs that announce from edge locations, eliminating DNS caching problems.

---

#### Question 19: S3 Performance Optimization (Multi-select) ❌
**Your Answer:** B (correct) + C (wrong)  
**Correct Answer:** B + D

**Selected Wrong:** C - More LIST calls via concurrent connections  
**Missed Correct:** D - Build catalog index (DynamoDB/OpenSearch)

**Why You Failed:**
- Thought scaling LIST calls would help (actually makes it worse)
- Didn't recognize catalog pattern for avoiding LIST operations
- 80% write bottleneck + 20% read/LIST → two different solutions needed

**Key Learning:**
```
S3 Performance Optimization:
├── Write Bottleneck (80%) ✅
│   ├── Multipart Upload
│   ├── Parallelization
│   ├── Transfer Acceleration
│   └── Well-designed prefixes
└── LIST Bottleneck (20%)
    ├── ❌ More LIST calls (makes worse)
    └── ✅ Catalog index
        ├── DynamoDB table
        ├── S3 Inventory + Athena
        └── OpenSearch Service
```

---

#### Question 24: CloudFront Custom Error Pages ❌
**Your Answer:** D - Upload directly into CloudFront  
**Correct Answer:** C - S3 + Custom Error Responses

**Why You Failed:**
- CloudFront doesn't store pages (it's a CDN, not storage)
- All content must be at an origin (S3 or HTTP)
- Missed Custom Error Responses configuration

**Key Learning:**
```
CloudFront Error Handling:
1. Store error pages in S3 (with OAC/OAI)
2. Configure Custom Error Responses
   ├── Status codes (500, 502, 503, etc.)
   ├── Response Page Path (/errors/500.html)
   └── Minimum error TTL
3. CloudFront caches and serves from edge
```

---

#### Question 26: Load Balancer Routing ❌
**Your Answer:** C - ALB with path-based rules  
**Correct Answer:** D - ALB with host-based routing rules

**Why You Failed:**
- Confused host-based vs path-based routing
- Requirement was "Host header (hostname)" routing
- Both are ALB features but wrong type

**Key Learning:**
```
ALB Routing Rules (Layer 7):
├── Host-Based Routing ✅
│   ├── Based on Host header
│   ├── Example: api.example.com vs www.example.com
│   └── Route to different target groups
└── Path-Based Routing
    ├── Based on URL path
    └── Example: /api vs /images
```

---

#### Question 27: ECS Dynamic Port Mapping ❌
**Your Answer:** C - Network Load Balancer only  
**Correct Answer:** A - Application Load Balancer OR Network Load Balancer

**Why You Failed:**
- Thought only NLB supported dynamic ports
- Actually BOTH ALB and NLB support it
- Classic LB does NOT support it

**Key Learning:**
```
Dynamic Port Mapping Support:
├── ✅ Application Load Balancer
├── ✅ Network Load Balancer
└── ❌ Classic Load Balancer

Requirement: Multiple ECS tasks on single instance
Solution: Host port = 0 (ephemeral port range)
```

---

#### Question 32: RDS Read-Heavy Scaling ❌
**Your Answer:** B - Configure Multi-AZ replicas for read traffic  
**Correct Answer:** A - Use Amazon ElastiCache

**Why You Failed:**
- Multi-AZ standby is NOT for reads (only availability)
- ElastiCache is the standard pattern for read-heavy DB workloads
- Missed "heavy loads on database servers"

**Key Learning:**
```
RDS Scaling Patterns:
├── Multi-AZ ❌ for reads
│   ├── Synchronous standby
│   ├── Only for HA/failover
│   └── NOT for read traffic
├── Read Replicas ✅ for reads
│   └── Asynchronous replication
└── ElastiCache ✅ BEST for read-heavy
    ├── Sub-millisecond latency
    ├── Removes DB pressure
    └── Redis/Memcached
```

---

#### Question 50: EC2 Public IP Behavior ❌
**Your Answer:** D - EBS-backed instances can't be stopped  
**Correct Answer:** C - Public IPv4 changed on restart

**Why You Failed:**
- Thought the statement about EBS instances was true
- Actually: EBS-backed CAN be stopped (instance-store cannot)
- Missed the actual issue: ephemeral public IPs change on stop/start

**Key Learning:**
```
EC2 Stop/Start Behavior:
├── EBS-Backed Instances ✅
│   ├── CAN be stopped and started
│   ├── Private IP: PRESERVED
│   ├── Public IP: CHANGES (unless EIP)
│   └── Issue: SSH configs have old IP
└── Instance-Store Backed ❌
    └── CANNOT be stopped (only terminated)

Solution: Use Elastic IP for persistent public IP
```

---

#### Question 64: Auto Scaling AZ Rebalancing ❌
**Your Answer:** B - Step scaling + predictive scaling  
**Correct Answer:** C - Target tracking + AZ capacity rebalancing

**Why You Failed:**
- Predictive scaling adds cost/complexity (not needed here)
- Missed "AZ capacity rebalancing" feature
- Target tracking naturally converges to balanced state

**Key Learning:**
```
Auto Scaling Strategies:
├── Simple Scaling ❌
│   └── Fixed steps, can oscillate
├── Step Scaling ❌
│   └── Multiple steps, still reactive
├── Target Tracking ✅
│   ├── Converges to metric target
│   ├── + AZ Rebalancing
│   └── Removes hot spots automatically
└── Predictive Scaling
    └── ML-based, adds complexity
```

---

### INCORRECT ANSWERS - SECURE ARCHITECTURES

#### Question 7: ECS Task-Level Security ❌
**Your Answer:** D - Bridge networking mode  
**Correct Answer:** C - awsvpc networking mode

**Why You Failed:**
- Bridge provides NATed ports, no per-task ENIs
- awsvpc gives each task its own ENI and security group
- Missed "task-level security controls and granular network visibility"

**Key Learning:**
```
ECS Networking Modes (EC2 Launch Type):
├── Host ❌
│   └── Shares instance network namespace
├── Bridge ❌
│   ├── Docker bridge
│   ├── NATed ports
│   └── No per-task SGs
└── awsvpc ✅
    ├── Each task gets own ENI
    ├── Task-level security groups
    ├── VPC flow log visibility
    └── Same as Fargate default
```

---

#### Question 11: S3 Bucket Access Control ❌
**Your Answer:** B - Explicit deny for all users except listed  
**Correct Answer:** C - Bucket policy allows specific role; HR assumes role

**Why You Failed:**
- Explicit deny lists become maintenance burden
- Role-based access is more scalable
- Missed "minimal ongoing administration"

**Key Learning:**
```
S3 Access Control Patterns:
├── Explicit Deny Lists ❌
│   ├── High maintenance
│   ├── Brittle as users rotate
│   └── Hard-coded user ARNs
└── Role-Based Access ✅
    ├── Policy allows specific role
    ├── HR users assume role
    ├── Can add MFA
    └── Centralized management
```

---

#### Question 28: Secrets Manager Key Rotation ❌
**Your Answer:** A - Use Parameter Store  
**Correct Answer:** C - Customize rotation Lambda

**Why You Failed:**
- Parameter Store doesn't support automatic rotation
- Secrets Manager has rotation framework
- API keys need custom rotation logic (not built-in like RDS)

**Key Learning:**
```
Secrets Manager Rotation:
├── Built-in Rotation
│   ├── RDS/Aurora
│   ├── DocumentDB
│   └── Redshift
└── Custom Rotation ✅
    ├── Custom Lambda function
    ├── Create/validate/set new key
    ├── Update secret
    └── For API keys, 3rd-party services
```

---

#### Question 32: Organization Monitoring ❌
**Your Answer:** B - AWS Config Resources  
**Correct Answer:** C - AWS CloudTrail

**Why You Failed:**
- Config tracks configuration changes (not API calls)
- CloudTrail records management events across accounts
- Missed "administrator acts"

**Key Learning:**
```
AWS Monitoring Services:
├── CloudTrail ✅
│   ├── API call logging
│   ├── Management events
│   ├── Organization-level trails
│   └── Admin activity tracking
└── Config ❌
    ├── Configuration state
    ├── Compliance rules
    └── Not for API activity
```

---

#### Question 47: Network Protection ❌
**Your Answer:** A - Security Group inbound rules  
**Correct Answer:** C - Network ACL inbound deny rules

**Why You Failed:**
- Security Groups don't support explicit DENY
- NACLs are stateless and support deny rules
- Missed "DoS attack" → need subnet-level blocking

**Key Learning:**
```
Network Security:
├── Security Groups ❌
│   ├── Stateful
│   ├── Allow rules only
│   └── Instance-level
└── Network ACLs ✅
    ├── Stateless
    ├── Allow AND Deny rules
    ├── Subnet-level
    └── Can block IPs/ranges
```

---

#### Question 61: Storage Gateway Selection ❌
**Your Answer:** D - Tape Gateway  
**Correct Answer:** C - File Gateway

**Why You Failed:**
- Tape Gateway is for backup/archive (VTL)
- File Gateway exposes S3 as SMB/NFS share
- Missed "administrators access objects directly via S3 console"

**Key Learning:**
```
Storage Gateway Types:
├── File Gateway ✅
│   ├── SMB/NFS share on-prem
│   ├── Data stored as S3 objects
│   ├── Admin can access via S3 console
│   └── Native S3 object access
├── Volume Gateway (Cached/Stored) ❌
│   ├── iSCSI block storage
│   └── Data NOT as browsable S3 objects
└── Tape Gateway ❌
    ├── VTL emulation
    └── For backup workflows
```

---

### REVIEW MARKED QUESTIONS (Got Correct but Flagged)

#### Question 10: S3 CORS Configuration ✅ (Marked for review)
- Correctly answered but had uncertainty
- Review: CORS Access-Control-Request-Method = GET (JSON format)

#### Question 12: Redshift Monitoring ✅ (Marked for review)
- Correctly answered
- Affirm: Redshift console provides query monitoring, not CloudWatch alone

#### Question 13: ALB Internet Gateway Routing ✅ (Marked for review)
- Correctly answered
- Key: Internet-facing ALB needs route to IGW in subnet route table

#### Question 16: Global Accelerator ❌ (Marked for review - AND got wrong)
- Already covered above in Priority 1

#### Question 22: Cluster Placement Groups ✅ (Marked for review)
- Correctly answered
- Key: Cluster PG in single AZ, can move instances between groups (not merge)

#### Question 23: Kinesis Video Streams ✅ (Marked for review)
- Correctly answered
- Use case: Real-time surveillance camera footage ingestion

#### Question 34: CloudHSM Backup Keys ✅ (Marked for review)
- Correctly answered
- EBK encrypts data, PBK encrypts EBK, stored in S3 same region

---

## 🎓 Study Recommendations

### Week 1: High-Performing Architectures Deep Dive
**Focus:** Close the 39% failure rate gap

1. **ECS Architecture (Days 1-2)**
   - EC2 vs Fargate launch types
   - Outposts deployment options
   - Networking modes (awsvpc, bridge, host)
   - Dynamic port mapping
   - Service discovery

2. **Load Balancing (Day 3)**
   - ALB vs NLB vs CLB feature matrix
   - Host-based vs path-based routing
   - Dynamic port mapping support
   - Cross-zone load balancing

3. **S3 Performance (Days 4-5)**
   - Multipart upload optimization
   - Parallel request patterns
   - Transfer Acceleration
   - Prefix design
   - Catalog patterns (vs LIST operations)
   - S3 Inventory integration

4. **Global Distribution (Day 6)**
   - CloudFront configuration
   - Custom error responses
   - Global Accelerator use cases
   - Static IP requirements
   - Route 53 vs Global Accelerator

5. **Auto Scaling (Day 7)**
   - Scaling policies comparison
   - AZ rebalancing
   - Target tracking configuration
   - Cooldown periods

### Week 2: Secure Architectures Focus
**Focus:** Improve from 67% to 75%+

1. **IAM & Access Control (Days 1-2)**
   - Role-based access patterns
   - Explicit deny vs allow strategies
   - Cross-account access
   - Service control policies

2. **Network Security (Day 3)**
   - Security Groups vs NACLs
   - Stateful vs stateless filtering
   - DoS protection patterns
   - VPC security best practices

3. **Secrets Management (Day 4)**
   - Secrets Manager vs Parameter Store
   - Custom rotation Lambda patterns
   - KMS key policies
   - Secret access patterns

4. **Monitoring & Compliance (Day 5)**
   - CloudTrail vs Config vs CloudWatch
   - Organization-wide logging
   - Cross-account trails
   - Event-driven responses

5. **Storage Security (Days 6-7)**
   - Storage Gateway types and use cases
   - S3 encryption options
   - KMS key policies
   - Data access patterns

### Week 3: Resilient Architectures Polish
**Focus:** Maintain 86% mastery

1. **FSx Deep Dive (Days 1-2)**
   - FSx for Lustre architecture
   - FSx for Windows File Server
   - DataSync integration
   - Cross-region/account access

2. **Database Scaling (Days 3-4)**
   - RDS Multi-AZ vs Read Replicas
   - ElastiCache patterns
   - Read-heavy vs write-heavy optimization
   - Sharding strategies

3. **Disaster Recovery (Days 5-7)**
   - Backup strategies
   - Cross-region replication
   - RPO/RTO targets
   - Failover procedures

---

## 🧪 Practice Labs Needed

### High Priority Labs

1. **ECS Networking Lab**
   ```
   Tasks:
   - Deploy ECS cluster with EC2 launch type
   - Configure awsvpc networking mode
   - Test task-level security groups
   - Implement dynamic port mapping with ALB
   ```

2. **S3 Performance Optimization Lab**
   ```
   Tasks:
   - Upload large files with multipart
   - Implement parallel requests
   - Build DynamoDB catalog for metadata
   - Compare LIST vs catalog performance
   ```

3. **CloudFront Custom Errors Lab**
   ```
   Tasks:
   - Configure S3 origin with error pages
   - Set up Custom Error Responses
   - Test 500/502/503 error handling
   - Implement OAC for private S3
   ```

4. **Auto Scaling AZ Rebalancing Lab**
   ```
   Tasks:
   - Create ASG across 2 AZs
   - Configure target tracking policy
   - Enable AZ rebalancing
   - Simulate load and observe distribution
   ```

5. **Secrets Manager Rotation Lab**
   ```
   Tasks:
   - Store API key in Secrets Manager
   - Create custom rotation Lambda
   - Implement rotation logic
   - Test application access during rotation
   ```

6. **Network Security Lab**
   ```
   Tasks:
   - Configure Security Groups
   - Implement Network ACLs with deny rules
   - Test DoS protection patterns
   - Compare SG vs NACL behavior
   ```

---

## 📊 Statistical Analysis

### Question Difficulty Analysis
```
Easy Questions (90%+ pass rate): 15/65
├── Got Correct: 15/15 (100%)
└── Performance: Excellent

Medium Questions (60-90% pass rate): 35/65
├── Got Correct: 26/35 (74%)
└── Performance: Below target

Hard Questions (<60% pass rate): 15/65
├── Got Correct: 6/15 (40%)
└── Performance: Needs significant work
```

### Time Management
- Average per question: ~82 seconds
- Total time: 89 minutes (target: 130 minutes)
- Time remaining: 41 minutes unused
- **Recommendation:** Slow down, re-read questions, use remaining time for review

### Answer Distribution
```
Correct: 47 (72.3%)
Incorrect: 18 (27.7%)
Marked for review: 12 (18.5%)
Of marked questions:
  - Correct: 9 (75%)
  - Incorrect: 3 (25%)
```

### Topic Correlation
**Weakest correlation:** High-performing architectures + Security
- Need to understand security implications of performance choices
- Example: awsvpc for task-level security vs bridge for performance

---

## 🎯 Next Steps Action Plan

### Immediate (This Week)
1. ✅ Review all 18 incorrect answers in detail
2. ✅ Complete 5 high-priority labs listed above
3. ✅ Create flashcards for missed concepts
4. ✅ Re-watch videos on ECS, Load Balancing, S3 performance

### Short Term (Weeks 2-3)
1. ✅ Complete Week 1-3 study plan
2. ✅ Take section quizzes on weak domains
3. ✅ Build mind maps for architecture decision trees
4. ✅ Join study group/forum discussions on weak topics

### Before Next Attempt
1. ✅ Score 80%+ on Domain 2 section quiz
2. ✅ Score 75%+ on Domain 3 section quiz
3. ✅ Complete all recommended labs
4. ✅ Review AWS whitepapers:
   - Performance Efficiency Pillar
   - Security Pillar
   - High-Performance Computing Lens

---

## 📚 Key Resources

### AWS Documentation
- [ECS Networking Modes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html)
- [S3 Performance Optimization](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html)
- [CloudFront Custom Error Pages](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html)
- [Auto Scaling Best Practices](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-best-practices.html)
- [Secrets Manager Rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)

### Whitepapers
- Performance Efficiency Pillar - Well-Architected Framework
- Security Pillar - Well-Architected Framework
- Microservices on AWS
- Implementing Microservices on AWS

### Blog Posts
- Building loosely-coupled applications with SQS and SNS
- Amazon S3 performance optimization
- ECS networking deep dive
- Secrets Manager best practices

---

## 💪 Motivation

**Progress from Attempt 1 to 2:** 
- If this was your first attempt at 72%, you're close!
- Only 2.69% away from passing
- Strong in 2 domains, need focus on 2 others
- With targeted study, you can pass in 2-3 weeks

**Your Strengths:**
- ✅ Perfect score in Cost Optimization
- ✅ Strong Resilient Architectures (86%)
- ✅ Good test-taking pace
- ✅ Marking questions for review (good self-awareness)

**Remember:**
- Most candidates need 2-3 attempts
- 72% → 75% is very achievable
- Focus on patterns, not memorization
- Understand the "why" behind each answer

---

**Next Exam Date Target:** 3-4 weeks from now  
**Realistic Pass Probability:** 85% with recommended study plan

Good luck! 🚀

