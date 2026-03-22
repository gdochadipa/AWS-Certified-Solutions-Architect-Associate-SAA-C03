# AWS SAA-C03 Practice Test 7 - Condensed Review
**Test Date:** March 6, 2026 | **Attempt:** 1st | **Score:** 48/65 (73.85%) ⚠️ BORDERLINE

---

## 📊 Quick Summary

| Domain | Score | Change from Test 6 |
|--------|-------|-------------------|
| **Resilient Architectures** | 11/17 (64.71%) | ❌ +3.6% (still failing) |
| **High-Performing Architectures** | 15/15 (100%) | ✅ +22% (PERFECT!) |
| **Secure Architectures** | 13/20 (65%) | ❌ -35% (MAJOR REGRESSION) |
| **Cost-Optimized Architectures** | 9/13 (69.23%) | ❌ -30.77% (MAJOR REGRESSION) |

**Overall:** 73.85% vs Test 6: 80% → **-6.15% REGRESSION** ⚠️

**Time Used:** 100/130 minutes | **Questions Marked:** 16 (24.6%)

**Status:** BORDERLINE PASS - Only 1.15% below real exam threshold!

---

## 🚨 CRITICAL: Regression Alert

### What Went Wrong?
- ❌ **Severe regression** in Security (-35%) and Cost (-30.77%)
- ❌ **More mistakes:** 17 incorrect vs 13 in Test 6
- ❌ **Three domains below 75%** (only one above in Test 7)
- ✅ **One bright spot:** High-Performing went from 78% → 100%

### Root Causes:
1. Didn't review Test 6 mistakes thoroughly
2. Focused only on High-Performing domain
3. Knowledge decay in Security/Cost domains
4. Fundamental gaps in KMS, Directory Services, pricing

---

## 🚨 Critical Failures (17 Questions)

### Domain 1: Resilient Architectures (6 failures)

#### ❌ Q1: Direct Connect BGP Community Tags
**Mistake:** Selected Local preference BGP (not supported on public VIF)  
**Fix:** Use BGP community tag 7224:9100 for local region only  
**Key Learning:**
```
BGP Community Tags (Public VIF):
├── 7224:9100 → Local region only ✅
├── 7224:9200 → All regions in continent
├── 7224:9300 → Global (all regions)
└── Local preference → Private/Transit VIF only ❌
```

#### ❌ Q4: AWS DataSync for EFS Cross-Region
**Mistake:** Manual S3 intermediate copy approach  
**Fix:** Use AWS DataSync directly between EFS  
**Key:** DataSync = purpose-built, no public network, automated

#### ❌ Q10: Backend Security Group Source
**Mistake:** Selected public subnet IP range  
**Fix:** Use frontend security group ID as source  
**Key:** SG-to-SG reference allows dynamic instance scaling

#### ❌ Q16: NAT Gateway Cost Optimization
**Mistake:** Selected Private NAT Gateway  
**Fix:** Public NAT Gateway per AZ (eliminates cross-AZ charges)  
**Key Learning:**
```
NAT Gateway Types:
├── Public NAT → Internet access (needs EIP) ✅
└── Private NAT → VPC/on-premises connectivity ❌
Cost Saving: Deploy per AZ to avoid cross-AZ data transfer
```

#### ❌ Q19: EBS Snapshot Cross-Region
**Mistake:** Copy to S3 bucket + enable CRR  
**Fix:** Use native "Copy Snapshot" feature  
**Key:** EBS snapshots already in S3 (AWS-managed), no CRR needed

#### ❌ Q46: EC2 Network Interface for Management
**Mistake:** Different subnets for complexity  
**Fix:** Secondary ENI in same subnet with management SG  
**Key:** Same subnet works, separation via security groups

---

### Domain 2: High-Performing Architectures (0 failures!)
**🎉 PERFECT SCORE: 15/15 (100%)**

All correct! Topics mastered:
- ✅ DynamoDB + ElastiCache for session data
- ✅ AWS DataSync for EFS transfer
- ✅ Amazon Comprehend for NLP
- ✅ EC2 metadata for AMI-ID retrieval
- ✅ SQS queue depth for ECS scaling
- ✅ Auto Scaling lifecycle hooks
- ✅ S3 Select SQL expression limits (256 KB)
- ✅ Amazon Kinesis for GPS data ingestion
- ✅ AWS Lake Formation for data lakes
- ✅ Amazon Rekognition Custom Labels for wildlife

**Keep doing what you're doing in this domain!**

---

### Domain 3: Secure Architectures (7 failures) - WORST REGRESSION

#### ❌ Q6: Systems Manager vs Secrets Manager
**Mistake:** Selected Secrets Manager for AMI IDs/license keys  
**Fix:** Use Parameter Store (config data) vs Secrets Manager (credentials)  
**Key Decision:**
```
AWS Secrets Manager → Database passwords, API keys
Parameter Store → AMI IDs, license keys, config ✅
```

#### ❌ Q8: FSx for Windows File Server
**Mistake:** S3 + AD Connector  
**Fix:** Amazon FSx for Windows File Server (native AD integration)  
**Key:** AD Connector = proxy, not file server

#### ❌ Q30: EC2 Networking awsvpc Mode
**Mistake:** Selected host networking mode  
**Fix:** awsvpc mode gives each task separate ENI + security group  
**Key:** awsvpc = granular network monitoring per task

#### ❌ Q34: Oracle RDS TDE with CloudHSM
**Mistake:** Selected MariaDB  
**Fix:** Oracle or SQL Server (only engines supporting TDE)  
**Key Learning:**
```
RDS TDE Support:
├── Oracle Enterprise Edition ✅
├── SQL Server Enterprise Edition ✅
└── MySQL, MariaDB, PostgreSQL ❌
```

#### ❌ Q35: Redshift Enable Encryption
**Mistake:** Create new cluster and migrate  
**Fix:** Enable encryption on existing cluster (modern feature)  
**Key:** Redshift auto-migrates data when enabling encryption (since 2019)

#### ❌ Q37: CloudFront Signed Cookies
**Mistake:** "S3 Signed Cookies" (doesn't exist!)  
**Fix:** CloudFront Signed Cookies for multiple files  
**Key Decision:**
```
CloudFront Signed URLs → Single file access
CloudFront Signed Cookies → Multiple files, same URL ✅
S3 Presigned URLs → Direct S3 access (bypasses CF)
```

#### ❌ Q41: KMS Multi-Region Keys
**Mistake:** Thought KMS keys are global  
**Fix:** Keys are region-specific; use Multi-Region Keys for global apps  
**Key Learning:**
```
KMS Architecture:
├── Single-Region Keys (default) → Region-locked
├── Multi-Region Keys → Same key ID across regions ✅
└── CRITICAL: Keys are NEVER global by default!
```

---

### Domain 4: Cost-Optimized Architectures (4 failures)

#### ❌ Q23: Spot Instances vs Savings Plans
**Mistake:** Selected Savings Plans for spiky traffic  
**Fix:** Use Spot Instances (up to 90% off, fault-tolerant)  
**Key Decision Matrix:**
```
Workload Type → Best Option → Discount
─────────────────────────────────────────
Steady baseline → Reserved/Savings → 72%
Spiky + fault-tolerant → Spot ✅ → 90%
Unpredictable → On-Demand → 0%
```

#### ❌ Q42: EBS Snapshot Archive (Got correct, but marked for review)
**Learning:** EBS Snapshot Archive = 75% cost savings for long-term retention  
**Key:** Use for compliance, rarely accessed backups (24-72h restore)

#### ❌ Q47: AWS Batch Job Stuck in RUNNABLE
**Mistake:** Selected "use ECS-optimized AMI"  
**Fix:** Ensure awslogs driver is configured  
**Key:** Missing awslogs driver prevents job placement (even with resources)

#### ❌ Q50: EC2 Instance Savings Plan vs Compute
**Mistake:** Selected Compute Savings Plan  
**Fix:** EC2 Instance Savings Plan (72% vs 66% discount)  
**Key Learning:**
```
Savings Plans Comparison:
├── EC2 Instance → 72% discount ✅ (same family)
└── Compute → 66% discount (flexibility across families)

Question: "4 M5.large, very consistent, max savings"
Answer: EC2 Instance Savings Plan ✅
```

---

## 🎯 URGENT Priority Study Topics

### 🔴 CRITICAL (Study First - Fundamental Gaps)
- [ ] **KMS Multi-Region Keys** (thought keys were global - FALSE!)
- [ ] **Directory Services:** Simple AD vs AD Connector vs Managed AD
- [ ] **EC2 Pricing Models:** Spot vs Savings Plans vs Reserved Instances
- [ ] **Storage Gateway Types:** S3 File vs Tape vs Volume vs FSx
- [ ] **CloudFront Access Control:** Signed URLs vs Signed Cookies

### 🟡 HIGH (Major Mistakes)
- [ ] NAT Gateway types (Public vs Private) + cost optimization
- [ ] RDS TDE support (Oracle/SQL only)
- [ ] Redshift encryption (can enable on existing cluster)
- [ ] Parameter Store vs Secrets Manager use cases
- [ ] Direct Connect BGP community tags

### 🟢 MEDIUM (Review)
- [ ] AWS DataSync for cross-region EFS transfer
- [ ] EBS snapshot cross-region copy (native feature)
- [ ] EC2 secondary network interfaces
- [ ] AWS Batch job states and troubleshooting
- [ ] EBS Snapshot Archive tier

---

## 📝 Must-Do Labs (Complete Before Next Test)

### Priority 1 (Urgent):
1. **KMS Multi-Region Keys Lab**
   - Create primary key in us-east-1
   - Replicate to eu-west-1, ap-south-1
   - Encrypt in one region, decrypt in another
   - Verify key ID consistency

2. **Directory Services Lab**
   - Launch Simple AD (~$36/month)
   - Create users (<500 limit)
   - Test AWS Console login
   - Compare with AD Connector (requires on-prem AD)

3. **Storage Gateway Lab**
   - Deploy S3 File Gateway (NFS/SMB protocols)
   - Compare with Tape Gateway (iSCSI-VTL)
   - Test file uploads, verify in S3
   - Enable S3 CRR for multi-region

### Priority 2:
4. **EC2 Pricing Models Lab**
   - Launch On-Demand instance (baseline cost)
   - Request Spot instance (handle interruption)
   - Calculate Savings Plan commitment
   - Compare 1-year costs

5. **NAT Gateway Lab**
   - Single NAT Gateway (multiple AZ subnets)
   - Monitor cross-AZ data transfer charges
   - Deploy NAT Gateway per AZ
   - Calculate cost difference

6. **CloudFront Access Control Lab**
   - Create signed URL for single file
   - Configure signed cookies for multiple files
   - Test access without credentials
   - Understand use case differences

---

## 🧮 Critical Formulas & Cheat Sheets

### KMS Key Scope
```
Single-Region Key (Default):
├── Keys are region-specific
├── Cannot decrypt in other regions
└── Use case: Data stays in one region

Multi-Region Key:
├── Same key ID across regions ✅
├── Encrypt in us-east-1, decrypt in eu-west-1
└── Use case: Global apps, reduced latency
```

### NAT Gateway Types
```
Public NAT Gateway:
├── For: Internet access from private subnet ✅
├── Location: Public subnet
├── Requirements: Elastic IP
└── Route: 0.0.0.0/0 → NAT Gateway

Private NAT Gateway:
├── For: VPC-to-VPC or on-premises connectivity
├── Location: Private subnet
├── Requirements: No EIP needed
└── Use: Transit Gateway, VPC peering
```

### Directory Services Decision Tree
```
Need standalone AD in AWS?
├── <500 users, basic features, low cost
│   └── Simple AD ($36/mo) ✅
└── >500 users, Microsoft AD features
    └── AWS Managed Microsoft AD ($144/mo)

Have on-premises AD?
└── Extend to AWS without replication
    └── AD Connector (proxy) ✅

Consumer-facing app?
└── Web/mobile user pools
    └── Amazon Cognito ✅
```

### Storage Gateway Types
```
File Gateway:
├── S3 File Gateway: NFS/SMB → S3 ✅
└── FSx File Gateway: SMB → FSx for Windows

Volume Gateway:
└── iSCSI block storage → EBS snapshots

Tape Gateway:
└── iSCSI-VTL → S3 Glacier (backup)
```

### CloudFront Access Control
```
Restrict access to:
├── Single file → Signed URL
├── Multiple files, same URL → Signed Cookies ✅
└── Direct S3 access → Presigned URLs
```

### EC2 Pricing Decision Matrix
```
Workload Pattern → Best Option → Discount
───────────────────────────────────────────
Steady, same family → EC2 Instance SP → 72%
Steady, may change family → Compute SP → 66%
Spiky, fault-tolerant → Spot ✅ → 90%
Unpredictable → On-Demand → 0%
```

---

## 📊 Performance Comparison: Test 6 vs Test 7

| Metric | Test 6 | Test 7 | Change |
|--------|--------|--------|--------|
| **Overall** | 80% | 73.85% | ⬇️ -6.15% |
| **Incorrect** | 13 | 17 | ⬇️ +4 errors |
| **Resilient** | 61.11% | 64.71% | ⬆️ +3.6% |
| **High-Performing** | 77.78% | 100% | ⬆️ +22.22% ✅ |
| **Secure** | 100% | 65% | ⬇️ -35% ❌ |
| **Cost** | 100% | 69.23% | ⬇️ -30.77% ❌ |
| **Review Marked** | 32.3% | 24.6% | ⬆️ More confident |

**Key Insight:** You CAN achieve 100% (High-Performing proves it), but mastery isn't sticky (Security/Cost regression proves it). Need systematic review + labs!

---

## ✅ What You're Doing Right

- ✅ **Time management:** 100/130 minutes (good pacing)
- ✅ **High-Performing domain:** 100% (22% improvement!)
- ✅ **Proven ability:** Can achieve perfection when focused
- ✅ **Self-awareness:** Marked 16 questions (shows critical thinking)

---

## ❌ What Needs Urgent Attention

- ❌ **Knowledge retention:** Lost mastery in Security/Cost
- ❌ **Fundamental gaps:** KMS regional scope, Directory Services basics
- ❌ **Service selection:** Confused pricing models, gateway types
- ❌ **Study consistency:** Must review Test 6 + Test 7 mistakes together
- ❌ **Practice without review:** Taking tests without fixing root causes

---

## 🎯 Next Practice Test Goal (Test 8)

**Minimum Targets:**
- [ ] Overall score: **85%+** (vs 73.85%)
- [ ] Resilient Architectures: **80%+** (vs 64.71%)
- [ ] Secure Architectures: **85%+** (vs 65%)
- [ ] Cost-Optimized: **85%+** (vs 69.23%)
- [ ] High-Performing: **95%+** (maintain excellence)
- [ ] Total incorrect: **<10** (vs 17)
- [ ] **No domain below 75%**

**Timeline:** 7 days of intensive study (3-4 hours/day)

**Prerequisites Before Test 8:**
- [ ] Complete all 6 priority labs above
- [ ] Score 85%+ on Security section quiz
- [ ] Score 85%+ on Cost-Optimized section quiz
- [ ] Review Test 6 + Test 7 mistakes side-by-side
- [ ] Create and memorize all flashcards below

---

## 🗂️ Essential Flashcards (Create These!)

### Front: KMS Multi-Region Keys
**Back:** Keys are region-specific by default. Multi-Region Keys allow same key ID across regions for global apps. Reduces latency by using local replica.

### Front: Simple AD vs AD Connector
**Back:** Simple AD = standalone Samba-based AD (<500 users, $36/mo). AD Connector = proxy to on-premises AD (requires existing AD). Use Simple AD when no on-prem AD exists.

### Front: Public vs Private NAT Gateway
**Back:** Public NAT = Internet access (needs EIP, public subnet). Private NAT = VPC/on-prem connectivity (no EIP, private subnet). Deploy Public NAT per AZ to save cross-AZ charges.

### Front: TDE Support in RDS
**Back:** Only Oracle Enterprise Edition and SQL Server Enterprise Edition support Transparent Data Encryption. NOT supported: MySQL, MariaDB, PostgreSQL, Aurora.

### Front: Spot vs Savings Plans
**Back:** Spot = 90% off, fault-tolerant, spiky workload. EC2 Instance SP = 72% off, same family, steady. Compute SP = 66% off, flexible families. Savings Plans require commitment (not for spikes).

### Front: S3 File Gateway vs Tape Gateway
**Back:** S3 File Gateway = NFS/SMB protocols → S3 storage. Tape Gateway = iSCSI-VTL → S3 Glacier (tape backup replacement). Different protocols and use cases!

### Front: CloudFront Signed Cookies vs URLs
**Back:** Signed Cookies = multiple files, URL stays same (e.g., stock photo library). Signed URLs = single file access, URL changes per user. "S3 Signed Cookies" doesn't exist!

### Front: Parameter Store vs Secrets Manager
**Back:** Parameter Store = config data (AMI IDs, license keys, settings). Secrets Manager = credentials (DB passwords, API keys) with rotation. Parameter Store is often free!

---

## 📅 7-Day Intensive Recovery Plan

### Day 1-2: Security Architecture Recovery
- [ ] **Morning:** Study KMS Multi-Region Keys (2 hours)
- [ ] **Afternoon:** Directory Services comparison (2 hours)
- [ ] **Evening:** Complete KMS + Directory Services labs (2 hours)
- [ ] **Goal:** Understand fundamentals that caused 7 failures

### Day 3-4: Cost Optimization Intensive
- [ ] **Morning:** EC2 pricing models deep dive (2 hours)
- [ ] **Afternoon:** NAT Gateway types + cost optimization (2 hours)
- [ ] **Evening:** Complete pricing + NAT Gateway labs (2 hours)
- [ ] **Goal:** Master cost decisions that caused 4 failures

### Day 5-6: Resilient Architectures
- [ ] **Morning:** Direct Connect BGP, DataSync, EBS snapshots (3 hours)
- [ ] **Afternoon:** Storage Gateway types, network interfaces (2 hours)
- [ ] **Evening:** Complete remaining labs (2 hours)
- [ ] **Goal:** Close gap from 64.71% to 80%+

### Day 7: Review & Practice Test 8
- [ ] **Morning:** Review ALL flashcards, Test 6 + Test 7 mistakes (3 hours)
- [ ] **Afternoon:** Take Practice Test 8 (2 hours)
- [ ] **Target:** 85%+ overall, no domain below 75%

---

## 💡 Quick Reference - Top Mistakes to Avoid

### ❌ Common Wrong Assumptions (Fix These!)
1. "KMS keys are global" → NO! Region-specific by default
2. "S3 Signed Cookies exist" → NO! CloudFront Signed Cookies
3. "NAT Gateway = all types internet access" → NO! Public only
4. "All RDS engines support TDE" → NO! Oracle/SQL only
5. "Savings Plans for spiky traffic" → NO! Requires commitment
6. "AD Connector = standalone AD" → NO! Requires on-prem AD
7. "Secrets Manager for AMI IDs" → NO! Use Parameter Store
8. "EBS snapshots need S3 CRR" → NO! Native copy feature

### ✅ Decision-Making Shortcuts
- **Multiple files, same URL?** → CloudFront Signed Cookies
- **AMI IDs, license keys?** → Parameter Store
- **<500 users, no on-prem AD?** → Simple AD
- **Spiky + fault-tolerant?** → Spot Instances
- **Internet from private subnet?** → Public NAT Gateway
- **NFS/SMB to S3?** → S3 File Gateway
- **Global app encryption?** → KMS Multi-Region Keys

---

## 🚨 Readiness Assessment

### Current Status: ⚠️ NOT READY
**Score:** 73.85% (1.15% below passing threshold)  
**Trend:** Regression from Test 6 (-6.15%)  
**Risk:** High probability of failure on real exam

### Path to Readiness:
**Estimated Time:** 2-3 weeks of intensive study (4+ hours/day)

**Must Complete Before Real Exam:**
1. Score 85%+ on Practice Test 8
2. All domains above 75%
3. No more than 10 incorrect on any practice test
4. Complete all 6 priority labs
5. Score 90%+ on section quizzes (Security, Cost, Resilient)

**DO NOT schedule real exam yet!** Risk of failure is too high.

---

## 🎉 Remember

**You proved you can achieve 100%** in High-Performing Architectures!

**But you also proved:**
- Knowledge decays without review (Security: 100% → 65%)
- Need systematic study (not just practice tests)
- Fundamentals matter (KMS, Directory Services, NAT types)
- Labs are essential (theory isn't enough)

**The gap is closable, but requires:**
- 2-3 weeks of focused study
- Daily review of mistakes (Test 6 + Test 7)
- Hands-on labs (6 required)
- Systematic approach (not random practice tests)

---

## 📊 Score Prediction for Real Exam

**Based on Test 7 Performance:**
- **Likely Score:** 70-75% (FAIL or borderline)
- **Confidence:** Low (severe regression trend)
- **Recommendation:** **DELAY** exam by 2-3 weeks

**After Completing 7-Day Plan:**
- **Expected Test 8 Score:** 82-87%
- **Real Exam Prediction:** 78-83% (PASS likely)
- **Timeline:** 2 more weeks of refinement

---

## 🎯 Success Formula

```
Test 7 Score: 73.85%
Gap to 85%: +11.15%

Required Improvements:
├── Secure Architectures: +20% (65% → 85%)
├── Cost-Optimized: +15.77% (69.23% → 85%)
├── Resilient Architectures: +15.29% (64.71% → 80%)
└── High-Performing: Maintain 95%+ (100% → 95%+)

Focus Distribution:
├── 40% on Security (worst regression)
├── 30% on Cost-Optimized (major regression)
├── 20% on Resilient (persistent weakness)
└── 10% on High-Performing (maintain excellence)
```

---

**Final Message:** Stop taking practice tests! Fix the root causes first through labs and systematic review. Test 8 in 7 days, NOT tomorrow!

**You can do this - but only with the right approach.** 🚀

---

**Next Steps:**
1. ✅ Read this condensed guide
2. ✅ Compare Test 6 vs Test 7 mistakes
3. ✅ Create flashcards above
4. ✅ Start Day 1 of 7-day plan tomorrow
5. ❌ DO NOT take another practice test until completing the plan!

