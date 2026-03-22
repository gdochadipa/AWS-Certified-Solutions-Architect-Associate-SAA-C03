# AWS SAA-C03 Study Notes

> Consolidated study notes for weak areas and exam remediation

## 📚 Table of Contents
- [Key Concepts to Review](#key-concepts-to-review)
- [Service-Specific Notes](#service-specific-notes)
- [Common Mistakes & Corrections](#common-mistakes--corrections)
- [Best Practices](#best-practices)

---

## Key Concepts to Review

### Auto Scaling & High Availability
- **Cooldown Periods**: Prevents rapid scaling; suppresses additional scale-out actions until cooldown ends
- **Target Tracking**: Converges capacity to a metric (e.g., CPU %), combined with AZ rebalancing for even distribution
- **Health Checks**: ELB health checks continuously probe targets; ASG replaces unhealthy instances automatically

### Networking & Connectivity
- **VPC Endpoints**:
  - Gateway endpoints: S3 and DynamoDB (free, route table based)
  - Interface endpoints: Other services via PrivateLink (ENI-based, charged)
- **Placement Groups**:
  - Cluster: Same AZ, low latency (HPC workloads)
  - Spread: Different hardware, high availability
  - Partition: Grouped instances, distributed failures

### Storage & Data Management
- **S3 Consistency**: Strong read-after-write consistency for all operations
- **S3 Versioning**: Preserves all versions; delete markers instead of permanent deletion
- **EBS Multi-Attach**: io1/io2 only, same AZ, limited use cases

---

## Service-Specific Notes

### Amazon S3
- **Object Lock**: WORM model, requires versioning, set at bucket creation
- **Lifecycle Policies**: Automate transitions and expiration
- **Cross-Region Replication**: Requires versioning on source and destination
- **Server-Side Encryption**: SSE-S3, SSE-KMS, SSE-C options

### Amazon CloudFront
- **Signed URLs vs Cookies**: URLs for individual files, Cookies for multiple files
- **Custom Error Pages**: Configure in distribution settings, cached at edge
- **Invalidation**: Removes cached objects immediately (break-glass for urgent updates)

### AWS Lambda
- **Execution Role Permissions**: 
  - logs:CreateLogGroup, logs:CreateLogStream, logs:PutLogEvents
  - Service-specific permissions (S3, DynamoDB, etc.)
- **Memory Configuration**: Affects CPU, network, and cost
- **Concurrency**: Reserved vs provisioned concurrency

### Amazon RDS & Aurora
- **Multi-AZ**: Automatic failover, standby not for reads
- **Read Replicas**: Scale read traffic, can be in different regions
- **Aurora Serverless**: Auto-scaling capacity units (ACUs)

---

## Common Mistakes & Corrections

### ❌ Wrong: Using Multi-AZ replicas for read traffic
### ✅ Correct: Use Read Replicas for read scaling; Multi-AZ is for HA only

### ❌ Wrong: Assuming eventual consistency for S3
### ✅ Correct: S3 provides strong read-after-write consistency

### ❌ Wrong: Trying to attach EBS volumes across AZs
### ✅ Correct: Snapshot → Restore in target AZ

### ❌ Wrong: Using Security Groups for explicit deny rules
### ✅ Correct: Use Network ACLs for deny rules; SGs only allow

---

## Best Practices

### Cost Optimization
1. Use appropriate instance types and sizes
2. Leverage Reserved Instances and Savings Plans
3. Implement S3 Lifecycle policies
4. Use AWS Cost Explorer and Trusted Advisor

### Security
1. Enable encryption at rest and in transit
2. Use IAM roles instead of access keys
3. Implement least privilege access
4. Enable MFA for sensitive operations
5. Use AWS Secrets Manager for credential rotation

### Performance
1. Use ElastiCache for frequently accessed data
2. Implement CloudFront for global content delivery
3. Use appropriate DB instance types
4. Enable enhanced monitoring

### Resilience
1. Deploy across multiple AZs
2. Implement health checks and auto-recovery
3. Use Auto Scaling for dynamic capacity
4. Regular backup and disaster recovery testing

---

*Last Updated: March 2026*

