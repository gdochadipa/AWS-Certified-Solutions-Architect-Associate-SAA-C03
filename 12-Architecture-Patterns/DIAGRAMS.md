# Architecture Patterns - Mermaid Diagrams

## Well-Architected Framework Pillars

### AWS Well-Architected Framework

```mermaid
mindmap
    root((AWS Well-Architected&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Framework()
        Operational Excellence
            IaC CloudFormation
            Runbooks
            Learn from failures
            Observability
            Event-driven
        Security
            Defense in depth
            Identity IAM
            Detective controls
            Data protection KMS
            Incident response
        Reliability
            Foundations
            Workload architecture
            Change management
            Failure management
            Multi-AZ RDS
        Performance Efficiency
            Selection
            Review
            Monitoring CloudWatch
            Tradeoffs
            Serverless Lambda
        Cost Optimization
            Practice financial mgmt
            Expenditure awareness
            Cost-effective resources
            Manage demand/supply
            Reserved Instances
        Sustainability
            Understand impact
            Establish goals
            Maximize utilization
            Adopt new efficient services
            Reduce downstream impact
```

## High Availability Architectures

### Multi-AZ Web Application

```mermaid
graph TB
    Users[Users[ --> Route53["Route 53&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;DNS with Health Checks"[
    
    Route53 --> CloudFront["CloudFront&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Global CDN&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Edge caching"[
    
    CloudFront --> Shield["AWS Shield&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;DDoS Protection"[
    Shield --> WAF["AWS WAF&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Application firewall"[
    
    subgraph Region_us_east_1_Group["Region: us-east-1"[
        WAF --> ALB["Application Load Balancer&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Multi-AZ"[
        
        subgraph AZ_1a_Group["AZ-1a"[
            ASG1[Auto Scaling Group[
            Web1[Web Server 1[
            App1[App Server 1[
            
            ASG1 --> Web1
            Web1 --> App1
        end
        
        subgraph AZ_1b_Group["AZ-1b"[
            ASG2[Auto Scaling Group[
            Web2[Web Server 2[
            App2[App Server 2[
            
            ASG2 --> Web2
            Web2 --> App2
        end
        
        subgraph AZ_1c_Group["AZ-1c"[
            ASG3[Auto Scaling Group[
            Web3[Web Server 3[
            App3[App Server 3[
            
            ASG3 --> Web3
            Web3 --> App3
        end
        
        ALB --> Web1
        ALB --> Web2
        ALB --> Web3
        
        App1 --> RDS["RDS Multi-AZ&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Primary in AZ-1a&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Standby in AZ-1b"[
        App2 --> RDS
        App3 --> RDS
        
        App1 --> ElastiCache["ElastiCache Redis&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Cluster mode&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Multi-AZ"[
        App2 --> ElastiCache
        App3 --> ElastiCache
    end
    
    RDS --> S3["S3&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Static assets&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Backups"[
    
    CloudWatch["CloudWatch&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Monitoring & Alarms"[ -.Monitor.-> ALB
    CloudWatch -.Monitor.-> RDS
    CloudWatch -.Scale.-> ASG1
    
    classDef style1 fill:#8C4FFF
    class Route53 style1
    classDef style2 fill:#FF9900
    class ALB style2
    classDef style3 fill:#3B48CC
    class RDS style3
    classDef style4 fill:#569A31
    class S3 style4
```

### Multi-Region Active-Active

```mermaid
graph TB
    Users[Global Users[ --> Route53["Route 53&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Geolocation or Latency Routing"[
    
    subgraph Primary_Region_us_east_1_Group["Primary Region: us-east-1"[
        ALB1[Application Load Balancer[
        
        ASG1["Auto Scaling Group&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;EC2 Instances"[
        
        RDS1["Aurora Global Database&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Primary Region&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Read/Write"[
        
        S3_1["S3 Bucket&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;us-east-1"[
        
        ALB1 --> ASG1
        ASG1 --> RDS1
        ASG1 --> S3_1
    end
    
    subgraph Secondary_Region_eu_west_1_Group["Secondary Region: eu-west-1"[
        ALB2[Application Load Balancer[
        
        ASG2["Auto Scaling Group&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;EC2 Instances"[
        
        RDS2["Aurora Global Database&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Secondary Region&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Read/Write"[
        
        S3_2["S3 Bucket&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;eu-west-1"[
        
        ALB2 --> ASG2
        ASG2 --> RDS2
        ASG2 --> S3_2
    end
    
    Route53 -->|US Traffic| ALB1
    Route53 -->|EU Traffic| ALB2
    
    RDS1 <-.Async Replication<br/>< 1 second.-> RDS2
    S3_1 <-.S3 Cross-Region<br/>Replication.-> S3_2
    
    DynamoDB["DynamoDB Global Tables&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Multi-region, multi-active"[ --> ASG1
    DynamoDB --> ASG2
    
    Benefits["Benefits:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Low latency globally&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ High availability&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Disaster recovery&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Read/write in any region&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;⚠️ Increased cost"[
    
    classDef style1 fill:#8C4FFF
    class Route53 style1
    classDef style2 fill:#3B48CC
    class RDS1 style2
    classDef style3 fill:#3B48CC
    class RDS2 style3
```

## Disaster Recovery Patterns

### DR Strategies Comparison

```mermaid
graph TB
    subgraph Backup_Restore_Group["Backup & Restore"[
        BR["Backup & Restore&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;💰 Lowest cost&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;⏱️ RTO: Hours-Days&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;⏱️ RPO: Hours"[
        
        BR_Desc["• Data backed up to S3&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Restore when needed&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• AMIs, DB snapshots&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Manual or automated&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Use: Non-critical systems"[
    end
    
    subgraph Pilot_Light_Group["Pilot Light"[
        PL["Pilot Light&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;💰 Low cost&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;⏱️ RTO: Minutes-Hours&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;⏱️ RPO: Minutes"[
        
        PL_Desc["• Core services always running&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Database replication&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Scale up when needed&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Critical data ready&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Use: Core business systems"[
    end
    
    subgraph Warm_Standby_Group["Warm Standby"[
        WS["Warm Standby&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;💰 Medium cost&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;⏱️ RTO: Minutes&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;⏱️ RPO: Seconds"[
        
        WS_Desc["• Scaled-down version running&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• All services active&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Scale up for failover&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• DNS failover&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Use: Business-critical apps"[
    end
    
    subgraph Multi_Site_Active_Active_Group["Multi-Site Active/Active"[
        MS["Multi-Site&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;💰 Highest cost&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;⏱️ RTO: Real-time&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;⏱️ RPO: Near-zero"[
        
        MS_Desc["• Full production in multiple regions&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Active-active traffic&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Instant failover&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Route 53 routing&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Use: Mission-critical systems"[
    end
    
    BR --> PL
    PL --> WS
    WS --> MS
    
    Spectrum["Cost increases -&gt;&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;RTO/RPO decreases -&gt;"[
    
    classDef style1 fill:#569A31
    class BR style1
    classDef style2 fill:#FF9900
    class PL style2
    classDef style3 fill:#146EB4
    class WS style3
    classDef style4 fill:#C00
    class MS style4
```

### Pilot Light Architecture

```mermaid
graph TB
    subgraph Production_Region_us_east_1_Group["Production Region: us-east-1"[
        Prod["Production Environment&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Fully operational"[
        
        ProdApp["Application Servers&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Auto Scaling"[
        ProdDB["RDS Primary&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Read/Write"[
        ProdS3["S3 Bucket&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Application data"[
        
        Prod --> ProdApp
        Prod --> ProdDB
        Prod --> ProdS3
    end
    
    subgraph DR_Region_us_west_2_Group["DR Region: us-west-2"[
        DR["DR Environment&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Pilot Light"[
        
        DRCore["Core Services:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Database running&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Data replication active&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;❌ App servers stopped&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;❌ Minimal compute"[
        
        DRDB["RDS Replica&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Read-only replica&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Can be promoted"[
        DRS3["S3 Bucket&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Cross-region replication"[
        
        AMI["AMIs & Templates&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Ready to launch"[
        
        DR --> DRCore
        DR --> DRDB
        DR --> DRS3
        DR --> AMI
    end
    
    ProdDB -.Async Replication.-> DRDB
    ProdS3 -.Cross-Region Replication.-> DRS3
    
    Disaster[Disaster Event[ -.Triggers.-> Failover["Failover Process:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;1. Promote RDS replica&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;2. Launch app servers from AMI&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;3. Update Route 53 DNS&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;4. Scale to production capacity"[
    
    Failover --> DRCore
    
    Timeline["Timeline:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Normal: Only DB running&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Disaster: 10-30 minutes to full capacity"[
    
    classDef style1 fill:#569A31
    class Prod style1
    classDef style2 fill:#FF9900
    class DR style2
    classDef style3 fill:#C00
    class Disaster style3
```

## Serverless Architectures

### Serverless Web Application

```mermaid
graph TB
    Users[Users[ --> CloudFront["CloudFront&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;CDN"[
    
    CloudFront --> S3Web["S3&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Static Website&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;React/Angular/Vue"[
    
    S3Web --> API["API Gateway&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;REST or HTTP API&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;WebSocket"[
    
    API --> Cognito["Amazon Cognito&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;User authentication&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;JWT tokens"[
    
    API --> Lambda["Lambda Functions&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Business logic&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Node.js/Python"[
    
    Lambda --> DynamoDB["DynamoDB&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;NoSQL database&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;On-demand capacity"[
    
    Lambda --> S3Data["S3&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Object storage&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;User uploads"[
    
    DynamoDB --> Streams[DynamoDB Streams[
    Streams --> LambdaStream["Lambda&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Stream processing"[
    
    LambdaStream --> SES["Amazon SES&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Email notifications"[
    
    S3Data --> EventBridge[EventBridge[
    EventBridge --> LambdaEvent["Lambda&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Event processing"[
    
    CloudWatch["CloudWatch&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Logs & Metrics"[ -.Monitor.-> Lambda
    XRay["X-Ray&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Distributed tracing"[ -.Trace.-> Lambda
    
    Benefits["Benefits:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ No servers to manage&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Auto-scaling&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Pay per use&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ High availability built-in&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Fast development"[
    
    classDef style1 fill:#FF9900
    class API style1
    classDef style2 fill:#569A31
    class Lambda style2
    classDef style3 fill:#146EB4
    class DynamoDB style3
```

### Event-Driven Serverless

```mermaid
graph LR
    subgraph Event_Sources_Group["Event Sources"[
        S3["S3&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;File upload"[
        DDB["DynamoDB&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Table change"[
        SQS["SQS&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Message queue"[
        Schedule["EventBridge&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Schedule/Cron"[
    end
    
    subgraph Event_Processing_Group["Event Processing"[
        Lambda1["Lambda Function 1&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Image processing"[
        Lambda2["Lambda Function 2&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Data validation"[
        Lambda3["Lambda Function 3&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Notification"[
        Lambda4["Lambda Function 4&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Cleanup task"[
    end
    
    subgraph Orchestration_Group["Orchestration"[
        StepFunctions["Step Functions&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Workflow coordination&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Error handling"[
    end
    
    subgraph Destinations_Group["Destinations"[
        S3Out["S3&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Processed files"[
        SNS["SNS&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Notifications"[
        DDBOut["DynamoDB&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Results"[
        SQS_DLQ["SQS&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Dead letter queue"[
    end
    
    S3 -->|Trigger| Lambda1
    DDB -->|Stream| Lambda2
    SQS -->|Poll| Lambda3
    Schedule -->|Invoke| Lambda4
    
    Lambda1 --> StepFunctions
    Lambda2 --> StepFunctions
    
    StepFunctions --> S3Out
    StepFunctions --> SNS
    StepFunctions --> DDBOut
    
    Lambda1 -.Failures.-> SQS_DLQ
    Lambda2 -.Failures.-> SQS_DLQ
    
    classDef style1 fill:#FF9900
    class Lambda1 style1
    classDef style2 fill:#569A31
    class StepFunctions style2
```

## Microservices Patterns

### Container-Based Microservices

```mermaid
graph TB
    Users[Users[ --> ALB["Application&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Load Balancer"[
    
    subgraph Amazon_ECS_EKS_Cluster_Group["Amazon ECS/EKS Cluster"[
        ALB --> Service1["User Service&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;ECS Task&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Container"[
        ALB --> Service2["Product Service&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;ECS Task&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Container"[
        ALB --> Service3["Order Service&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;ECS Task&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Container"[
        
        Service1 --> ServiceMesh["AWS App Mesh&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Service mesh&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Traffic management"[
        Service2 --> ServiceMesh
        Service3 --> ServiceMesh
    end
    
    subgraph Data_Layer_Group["Data Layer"[
        Service1 --> DDB1["DynamoDB&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;User data"[
        Service2 --> RDS1["RDS&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Product catalog"[
        Service3 --> Aurora["Aurora&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Orders"[
    end
    
    subgraph Async_Communication_Group["Async Communication"[
        Service1 --> SNS[SNS Topic[
        SNS --> SQS1[SQS Queue 1[
        SNS --> SQS2[SQS Queue 2[
        
        SQS1 --> Service2
        SQS2 --> Service3
    end
    
    subgraph Service_Discovery_Group["Service Discovery"[
        CloudMap["AWS Cloud Map&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Service registry&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;DNS-based discovery"[
        
        Service1 -.Register.-> CloudMap
        Service2 -.Register.-> CloudMap
        Service3 -.Register.-> CloudMap
    end
    
    ECR["Amazon ECR&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Container registry"[ -.Pull images.-> Service1
    
    Observability["CloudWatch Container Insights&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;X-Ray tracing&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Centralized logging"[ -.Monitor.-> Service1
    
    classDef style1 fill:#FF9900
    class ServiceMesh style1
    classDef style2 fill:#569A31
    class CloudMap style2
```

### API-First Microservices

```mermaid
graph TB
    Mobile[Mobile Apps[ --> API["API Gateway&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Unified API"[
    Web[Web Apps[ --> API
    Partners[Partner APIs[ --> API
    
    subgraph API_Gateway_Features_Group["API Gateway Features"[
        Auth["Authorization&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Cognito/Lambda"[
        Cache[Response Caching[
        Throttle[Throttling & Quotas[
        Transform["Request/Response&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Transformation"[
        
        API --> Auth
        API --> Cache
        API --> Throttle
        API --> Transform
    end
    
    subgraph Microservices_Group["Microservices"[
        Lambda1["Lambda&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;User Service"[
        Lambda2["Lambda&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Product Service"[
        ECS["ECS&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Order Service"[
        EC2["EC2&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Legacy Service"[
    end
    
    subgraph Backend_for_Frontend_BFF_Group["Backend for Frontend BFF"[
        BFF_Mobile["Mobile BFF&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Optimized for mobile"[
        BFF_Web["Web BFF&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Optimized for web"[
    end
    
    Auth --> Lambda1
    Auth --> Lambda2
    Auth --> ECS
    Auth --> EC2
    
    Lambda1 --> BFF_Mobile
    Lambda2 --> BFF_Mobile
    ECS --> BFF_Web
    
    Lambda1 --> DDB[DynamoDB[
    Lambda2 --> S3[S3[
    ECS --> RDS[RDS[
    
    WAF[AWS WAF[ -.Protect.-> API
    Shield[AWS Shield[ -.DDoS Protection.-> API
    
    classDef style1 fill:#FF9900
    class API style1
    classDef style2 fill:#569A31
    class Lambda1 style2
```

## Data Lake Architecture

### Comprehensive Data Lake

```mermaid
graph TB
    subgraph Data_Sources_Group["Data Sources"[
        Streaming["Streaming Data&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Kinesis, IoT"[
        Batch["Batch Data&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Databases, Files"[
        RealTime["Real-time Apps&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;APIs, Logs"[
    end
    
    subgraph Ingestion_Layer_Group["Ingestion Layer"[
        Kinesis["Kinesis Firehose&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Streaming ingestion"[
        DataSync["AWS DataSync&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Batch transfer"[
        DMS["AWS DMS&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Database migration"[
    end
    
    subgraph Storage_Layer_S3_Group["Storage Layer - S3"[
        Raw["Raw Zone&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Landing area&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Original format&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;All data retained"[
        
        Processed["Processed Zone&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Cleaned & validated&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Parquet/ORC format&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Partitioned"[
        
        Curated["Curated Zone&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Business-ready&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Aggregated views&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Optimized for queries"[
    end
    
    subgraph Cataloging_Group["Cataloging"[
        Crawler["Glue Crawlers&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Schema discovery"[
        Catalog["Glue Data Catalog&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Metadata repository"[
        
        Crawler --> Catalog
    end
    
    subgraph Processing_Group["Processing"[
        Glue["AWS Glue&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;ETL jobs&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Serverless Spark"[
        
        EMR["Amazon EMR&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Complex analytics&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;ML processing"[
        
        Lambda["Lambda&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Real-time transforms"[
    end
    
    subgraph Analytics_ML_Group["Analytics & ML"[
        Athena["Athena&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Interactive SQL"[
        Redshift["Redshift Spectrum&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Data warehouse"[
        SageMaker["SageMaker&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Machine learning"[
        QuickSight["QuickSight&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;BI dashboards"[
    end
    
    Streaming --> Kinesis
    Batch --> DataSync
    Batch --> DMS
    
    Kinesis --> Raw
    DataSync --> Raw
    DMS --> Raw
    
    Raw --> Glue
    Glue --> Processed
    
    Processed --> EMR
    EMR --> Curated
    
    Raw --> Crawler
    Processed --> Crawler
    Curated --> Crawler
    
    Catalog --> Athena
    Catalog --> Redshift
    
    Curated --> Athena
    Curated --> Redshift
    Curated --> SageMaker
    
    Athena --> QuickSight
    Redshift --> QuickSight
    
    LakeFormation["AWS Lake Formation&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Centralized governance&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Access control&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Data quality"[ -.Governs.-> Raw
    
    classDef style1 fill:#C00
    class Raw style1
    classDef style2 fill:#FF9900
    class Processed style2
    classDef style3 fill:#569A31
    class Curated style3
    classDef style4 fill:#146EB4
    class Catalog style4
```

## Hybrid Cloud Patterns

### Hybrid Cloud Architecture

```mermaid
graph TB
    subgraph On_Premises_Data_Center_Group["On-Premises Data Center"[
        OnPrem[Corporate Network[
        AD[Active Directory[
        VMs[Virtual Machines[
        Storage[Storage Arrays[
        Apps[Legacy Applications[
    end
    
    subgraph AWS_Connectivity_Group["AWS Connectivity"[
        VPN["AWS VPN&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Encrypted tunnel"[
        DX["AWS Direct Connect&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Dedicated connection"[
        
        TGW["Transit Gateway&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Central hub"[
    end
    
    subgraph AWS_Cloud_Group["AWS Cloud"[
        subgraph VPC_Group["VPC"[
            PrivateSubnet[Private Subnets[
            Workloads[EC2 Workloads[
            
            PrivateSubnet --> Workloads
        end
        
        subgraph Hybrid_Services_Group["Hybrid Services"[
            DirectoryService["AWS Managed&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Microsoft AD&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Trust relationship"[
            
            StorageGW["Storage Gateway&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Hybrid storage"[
            
            Outposts["AWS Outposts&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;On-prem AWS"[
            
            VMware["VMware Cloud&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;on AWS"[
        end
        
        subgraph AWS_Services_Group["AWS Services"[
            S3[S3[
            RDS[RDS[
            Lambda[Lambda[
        end
    end
    
    OnPrem --> VPN
    OnPrem --> DX
    
    VPN --> TGW
    DX --> TGW
    
    TGW --> PrivateSubnet
    
    AD <-.Trust.-> DirectoryService
    Storage <-.Sync.-> StorageGW
    VMs -.Migrate.-> VMware
    
    StorageGW --> S3
    Workloads --> RDS
    Workloads --> Lambda
    
    SSM["Systems Manager&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Unified management"[ -.Manage.-> Workloads
    SSM -.Manage.-> OnPrem
    
    classDef style1 fill:#FF9900
    class TGW style1
    classDef style2 fill:#569A31
    class DirectoryService style2
    classDef style3 fill:#146EB4
    class DX style3
```

## Caching Strategies

### Multi-Layer Caching

```mermaid
graph TB
    User[User Request[ --> CF["CloudFront&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Edge Cache&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;TTL: Hours/Days&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Global distribution"[
    
    CF -->|Cache Miss| ALB["Application&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Load Balancer"[
    CF -->|Cache Hit| UserHit1["Return cached&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;response"[
    
    ALB --> AppServer["Application Server&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;EC2/ECS"[
    
    AppServer --> AppCache{"Application&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Cache Layer?"{
    
    AppCache -->|Check| ElastiCache["ElastiCache Redis&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;In-memory cache&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;TTL: Minutes/Hours&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Session data, objects"[
    
    ElastiCache -->|Cache Hit| AppServer
    ElastiCache -->|Cache Miss| DBQuery[Query Database[
    
    DBQuery --> RDS["RDS with&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Read Replicas&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Query cache enabled"[
    
    RDS --> ElastiCache
    ElastiCache --> AppServer
    AppServer --> CF
    CF --> User
    
    Strategies["Caching Strategies:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;CloudFront: Static content, API responses&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;ElastiCache: Session data, computed results&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;RDS: Query results&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Application: Business logic results&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Benefits:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Reduced latency&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Lower database load&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Cost savings&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Better user experience"[
    
    classDef style1 fill:#146EB4
    class CF style1
    classDef style2 fill:#C00
    class ElastiCache style2
    classDef style3 fill:#3B48CC
    class RDS style3
```

