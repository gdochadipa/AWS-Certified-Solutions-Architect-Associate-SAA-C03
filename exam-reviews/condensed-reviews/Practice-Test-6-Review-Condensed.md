# AWS SAA-C03 Practice Test 6 - Condensed Review
**Test Date:** March 5, 2026 | **Attempt:** 1st | **Score:** 52/65 (80%) ✅

---

## 📊 Quick Summary

| Domain | Score | Status |
|--------|-------|--------|
| **Resilient Architectures** | 11/18 (61%) | ❌ CRITICAL |
| **High-Performing Architectures** | 21/27 (78%) | ⚠️ REVIEW |
| **Secure Architectures** | 13/13 (100%) | ✅ PERFECT |
| **Cost-Optimized Architectures** | 7/7 (100%) | ✅ PERFECT |

**Time Used:** 97/130 minutes | **Questions Marked:** 21 (32%)

---

## 🚨 Critical Failures (13 Questions)

### Domain 1: Resilient Architectures (7 failures)

#### ❌ Q5: Site-to-Site VPN Prerequisites
**Mistake:** Selected NAT instance instead of VGW  
**Fix:** VPN needs VGW (AWS side) + Public IP on customer gateway  
**Key:** NAT = egress, VGW = VPN termination

#### ❌ Q6: EBS Performance
**Mistake:** Selected ELB for disk I/O improvement  
**Fix:** Larger instance type + Provisioned IOPS volumes  
**Key:** Instance type limits EBS bandwidth

#### ❌ Q25: Subnet CIDR Sizing
**Mistake:** /28 = 11 usable IPs (insufficient)  
**Fix:** /27 = 27 usable IPs (meets 20 instance requirement)  
**Key:** Formula: 2^(32-n) - 5 reserved IPs

```
Quick Reference:
/30 → 4 total - 5 = 0 usable
/29 → 8 total - 5 = 3 usable
/28 → 16 total - 5 = 11 usable ❌
/27 → 32 total - 5 = 27 usable ✅
```

#### ❌ Q35: DynamoDB Change Capture
**Mistake:** Duplicate table for tracking changes  
**Fix:** Use DynamoDB Streams for CDC  
**Key:** Streams = ordered, 24h retention, Lambda integration

#### ❌ Q36: RDS Parameter Groups
**Mistake:** Edit default parameter group  
**Fix:** Create custom parameter group (defaults are immutable)  
**Key:** Default = read-only, Custom = editable

#### ❌ Q42: S3 Storage Classes
**Mistake:** Thought one bucket = one storage class  
**Fix:** Each object can have different storage class  
**Key:** Standard (frequent) + One Zone-IA (infrequent, non-critical)

#### ❌ Q48: RDS Cost Optimization
**Mistake:** Switch to On-Demand (more expensive)  
**Fix:** Disable Multi-AZ in development environments  
**Key:** Multi-AZ doubles cost, only needed for production HA

#### ❌ Q58: ECS Container Bootstrap
**Mistake:** Task definition configures host OS  
**Fix:** EC2 User Data runs at instance boot  
**Key:** User Data = host config, Task Definition = container config

---

### Domain 2: High-Performing Architectures (6 failures)

#### ❌ Q11: S3 VPC Endpoint
**Mistake:** Create endpoint in VPC-B, peer to VPC-A  
**Fix:** Gateway endpoints NOT transitive, create in each VPC  
**Key:** Each VPC needs its own S3 gateway endpoint

#### ❌ Q46: EC2 Bootstrap
**Mistake:** Use EC2Config (legacy)  
**Fix:** Use User Data scripts (standard method)  
**Key:** User Data = cloud-init at first boot

#### ❌ Q49: Security Group Propagation
**Mistake:** Takes 2-5 minutes  
**Fix:** Changes apply instantly (no reboot needed)  
**Key:** SG rules are immediate, stateful

#### ❌ Q60: API Gateway Integrations
**Mistake:** Selected SFTP (not supported)  
**Fix:** Lambda cross-account, HTTP, VPC Link (all supported)  
**Key:** No direct DB, SFTP, or custom protocols

#### ❌ Q61: API Gateway Cache Key
**Mistake:** Use API Stage to split cache  
**Fix:** Query string parameters in cache key  
**Key:** ?type=equity vs ?type=fixed-income = separate cache entries

#### ❌ Q63: Lambda@Edge Events
**Mistake:** Selected "Sender Request" (doesn't exist)  
**Fix:** Viewer Request, Origin Request, Origin Response  
**Key:** 4 hooks: Viewer Req/Res, Origin Req/Res

---

## 🎯 Priority Study Topics

### 🔴 URGENT: VPC & Networking
- [ ] CIDR calculations (practice until automatic)
- [ ] VPC endpoints: Gateway vs Interface, per-VPC scope
- [ ] Site-to-Site VPN: VGW, Customer Gateway, IPsec
- [ ] Security Group instant propagation

### 🟡 HIGH: Storage & Database
- [ ] S3 storage classes (object-level, not bucket-level)
- [ ] DynamoDB Streams vs alternatives
- [ ] RDS parameter groups (default vs custom)
- [ ] RDS Multi-AZ cost optimization

### 🟢 MEDIUM: Compute & Integration
- [ ] EC2 User Data vs Task Definition vs Metadata
- [ ] EBS performance: instance type + volume type
- [ ] API Gateway: integrations, caching, cache keys
- [ ] Lambda@Edge: 4 event hooks

---

## 📝 Must-Do Labs

1. **VPC Lab:** Create VPC, calculate /27 /28 subnets, S3 gateway endpoint
2. **RDS Lab:** Custom parameter group, modify max_connections
3. **DynamoDB Lab:** Enable Streams, process with Lambda
4. **ECS Lab:** User data bootstrap, ECS agent config
5. **API Gateway Lab:** Cache key with query strings, VPC Link
6. **S3 Lab:** Objects in different storage classes (same bucket)

---

## 🧮 Critical Formulas

### Subnet Sizing
```
Total IPs = 2^(32 - CIDR_mask)
Usable IPs = Total - 5 (AWS reserves first 4 + last 1)

Need 20 instances? → /27 minimum (32-5=27 usable)
```

### EBS Performance
```
Actual IOPS/Throughput = MIN(
    Volume provisioned capacity,
    Instance EBS bandwidth limit
)
```

---

## ✅ Strengths to Maintain

- **Security:** 100% - Perfect understanding of encryption, IAM, VPC security
- **Cost Optimization:** 100% - Excellent judgment on RI, Spot, storage classes
- **Time Management:** 97/130 minutes - Good pacing with review time
- **Self-Assessment:** 32% marked for review shows critical thinking

---

## 📊 Performance Metrics

```
Overall: 80% (Pass: 75%) ✅ +5% margin

Domain Breakdown:
├── Resilient:        61% ❌ (Need 75%+)
├── High-Performing:  78% ⚠️  (Need 85%+)
├── Secure:          100% ✅ (Maintain)
└── Cost-Optimized:  100% ✅ (Maintain)

Time Analysis:
├── Total: 97 min (74% of allowed time)
├── Per Question: ~90 seconds
└── Review Time: 33 minutes remaining

Question Stats:
├── Easy (85%+): 24/25 correct (96%)
├── Medium (60-85%): 21/28 correct (75%)
└── Hard (<60%): 7/12 correct (58%)
```

---

## 🎯 Next Practice Test Goal

**Target Score:** 85%+ (55/65 questions)

**Focus Areas Before Next Attempt:**
1. Complete 6 priority labs above
2. Score 85%+ on Resilient Architectures section quiz
3. Master CIDR calculations
4. Review all 13 incorrect answers 3 times

**Timeline:** 2-3 weeks of focused study

---

## 💡 Quick Reference Cheat Sheet

### VPC Endpoints
- **Gateway:** S3, DynamoDB (per-VPC, not transitive)
- **Interface:** Most other services (PrivateLink, ENI-based)

### RDS Configuration
- **Parameter Group:** Engine settings (create custom to modify)
- **Option Group:** Engine features (e.g., Oracle options)
- **Multi-AZ:** Production only (doubles cost)

### DynamoDB Changes
- **Streams:** Ordered CDC, 24h retention ✅
- **Timestamp + Scan:** Expensive, no ordering ❌
- **Duplicate Table:** Maintenance burden ❌

### ECS Configuration Layers
- **User Data:** Host OS, runs at boot
- **Task Definition:** Container config (image, CPU, memory)
- **Service Definition:** Desired count, placement

### API Gateway
- **Cache Key:** Path, query strings, headers
- **Integrations:** Lambda (cross-account OK), HTTP, AWS services, VPC Link
- **NOT Supported:** Direct DB, SFTP, FTP

### Lambda@Edge Hooks
1. **Viewer Request:** Before cache lookup (auth, rewrite)
2. **Origin Request:** Before origin (cache miss)
3. **Origin Response:** After origin (header modification)
4. **Viewer Response:** Before viewer (final changes)

---

## 🎉 Achievement Unlocked

✅ **Passed on First Attempt!**  
✅ **Perfect Security Domain**  
✅ **Perfect Cost Optimization**  
✅ **Above 75% Threshold**

**Next Milestone:** 85%+ score with Resilient Architectures mastery

---

## 📅 Action Plan

### This Week
- [ ] Review this condensed guide daily
- [ ] Complete VPC & RDS labs
- [ ] Practice CIDR calculations (30 minutes/day)
- [ ] Read AWS docs on VPC endpoints

### Week 2
- [ ] Complete remaining labs (DynamoDB, ECS, API Gateway)
- [ ] Take Resilient Architectures section quiz
- [ ] Practice Lambda@Edge scenarios
- [ ] Build architecture decision trees

### Week 3
- [ ] Full practice test review
- [ ] Whiteboard architecture scenarios
- [ ] Timed question drills (40 questions in 60 minutes)
- [ ] Take Practice Test 6 - 2nd Attempt

---

**🎯 Remember:** You're 5% above passing. Close the Resilient Architectures gap (61%→85%) and you'll be ready for the real exam!

**Study Smart:** Focus 70% on weak areas, 30% on maintaining strengths.

Good luck! 🚀

