# Analytics - Mermaid Diagrams

## Amazon Athena

### Athena Architecture

```mermaid
graph TB
    subgraph Data_Sources_Group["Data Sources"[
        S3["S3 Data Lake&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;CSV, JSON, Parquet, ORC&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Partitioned data"[
        CloudTrail[CloudTrail Logs[
        VPCFlow[VPC Flow Logs[
        ELB_Logs[ELB Access Logs[
    end
    
    subgraph AWS_Athena_Group["AWS Athena"[
        Athena["Amazon Athena&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Serverless SQL queries&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Presto-based"[
        
        GlueCatalog["AWS Glue Data Catalog&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Table definitions&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Schema metadata"[
        
        Athena --> GlueCatalog
    end
    
    subgraph Query_Analysis_Group["Query & Analysis"[
        Query["SQL Queries&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;SELECT, JOIN, GROUP BY&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Standard SQL"[
        
        Results["Query Results&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Stored in S3"[
        
        Query --> Results
    end
    
    subgraph Visualization_Group["Visualization"[
        QuickSight["Amazon QuickSight&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Business intelligence"[
        JDBC["JDBC/ODBC&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;BI Tools&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Tableau, PowerBI"[
    end
    
    S3 --> GlueCatalog
    CloudTrail --> GlueCatalog
    VPCFlow --> GlueCatalog
    ELB_Logs --> GlueCatalog
    
    GlueCatalog --> Query
    
    Results --> QuickSight
    Results --> JDBC
    
    Features["Features:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Serverless - no infrastructure&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Pay per query $5 per TB scanned&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Supports partitioning&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Columnar formats for cost savings&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Federated queries&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;💡 Use Parquet for 90% cost reduction"[
    
    classDef style1 fill:#FF9900
    class Athena style1
    classDef style2 fill:#569A31
    class GlueCatalog style2
```

### Athena Performance Optimization

```mermaid
graph TB
    Original["Original S3 Data&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;CSV format&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;1 TB data&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;$5 per query"[
    
    Optimizations{"Performance&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Optimizations"{
    
    Original --> Optimizations
    
    Optimizations --> Partition["Partition Data&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;By year/month/day&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Only scan relevant partitions"[
    
    Optimizations --> Columnar["Use Columnar Format&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Parquet or ORC&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Only read needed columns"[
    
    Optimizations --> Compress["Compress Data&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Snappy, GZIP, LZO&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Smaller file sizes"[
    
    Optimizations --> Larger["Larger Files&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;&gt; 128 MB per file&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Reduce overhead"[
    
    Partition --> Result1["Scan only 1 month:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;83 GB instead of 1 TB&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;$0.42 per query&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;92% savings"[
    
    Columnar --> Result2["Select 2 of 10 columns:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;200 GB instead of 1 TB&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;$1 per query&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;80% savings"[
    
    Compress --> Result3["Compress by 50%:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;500 GB instead of 1 TB&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;$2.50 per query&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;50% savings"[
    
    Combined["Combined Optimizations:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Partition + Parquet + Compress&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;10 GB scanned&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;$0.05 per query&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;99% cost reduction!"[
    
    Result1 --> Combined
    Result2 --> Combined
    Result3 --> Combined
    
    classDef style1 fill:#C00
    class Original style1
    classDef style2 fill:#569A31
    class Combined style2
    classDef style3 fill:#FF9900
    class Optimizations style3
```

## Amazon EMR (Elastic MapReduce)

### EMR Cluster Architecture

```mermaid
graph TB
    subgraph EMR_Cluster_Group["EMR Cluster"[
        Master["Master Node&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Manage cluster&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Coordinate jobs&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Track status"[
        
        subgraph Core_Nodes_Group["Core Nodes"[
            Core1["Core Node 1&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Run tasks&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Store data in HDFS"[
            Core2["Core Node 2&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Run tasks&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Store data in HDFS"[
        end
        
        subgraph Task_Nodes_Optional_Group["Task Nodes Optional"[
            Task1["Task Node 1&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Run tasks only&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;No HDFS&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Spot instances OK"[
            Task2["Task Node 2&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Run tasks only&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;No HDFS&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Spot instances OK"[
        end
        
        Master --> Core1
        Master --> Core2
        Master --> Task1
        Master --> Task2
    end
    
    subgraph Storage_Group["Storage"[
        HDFS["HDFS&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Distributed file system&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;On core nodes"[
        
        EMRFS["EMRFS&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Access S3 as HDFS&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Persistent storage"[
    end
    
    subgraph Data_Sources_Targets_Group["Data Sources & Targets"[
        S3["Amazon S3&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Input & Output&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Persistent data"[
        
        DynamoDB["DynamoDB&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Read/Write"[
        
        RDS["RDS/Aurora&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;JDBC connections"[
    end
    
    Core1 --> HDFS
    Core2 --> HDFS
    
    Master --> EMRFS
    EMRFS --> S3
    
    Master --> DynamoDB
    Master --> RDS
    
    Frameworks["Big Data Frameworks:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Hadoop MapReduce&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Apache Spark&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Apache Hive&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Apache HBase&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Presto&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Flink&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Hudi"[
    
    classDef style1 fill:#FF9900
    class Master style1
    classDef style2 fill:#569A31
    class S3 style2
```

### EMR Deployment Options

```mermaid
graph TB
    EMR[Amazon EMR[
    
    EMR --> EC2["EMR on EC2&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Traditional clusters"[
    EMR --> EKS["EMR on EKS&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Kubernetes pods"[
    EMR --> Outposts["EMR on Outposts&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;On-premises"[
    EMR --> Serverless["EMR Serverless&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;No cluster management"[
    
    subgraph EMR_on_EC2_Group["EMR on EC2"[
        EC2_Features["• Full control&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Instance types&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Persistent or transient&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Spot instances&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Auto-scaling"[
    end
    
    subgraph EMR_on_EKS_Group["EMR on EKS"[
        EKS_Features["• Shared EKS cluster&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Multiple teams&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Better resource utilization&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Faster startup"[
    end
    
    subgraph EMR_Serverless_Group["EMR Serverless"[
        Serverless_Features["• No cluster management&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Auto-scaling&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Pay per use&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Sub-minute startup&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Ideal for: Ad-hoc, batch"[
    end
    
    EC2 --> EC2_Features
    EKS --> EKS_Features
    Serverless --> Serverless_Features
    
    Comparison["Choose:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Control needed -&gt; EC2&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Kubernetes -&gt; EKS&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Simplicity -&gt; Serverless"[
    
    classDef style1 fill:#FF9900
    class EMR style1
    classDef style2 fill:#569A31
    class Serverless style2
```

## Amazon Kinesis

### Kinesis Services Overview

```mermaid
mindmap
    root((Amazon Kinesis&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Real-time Streaming()
        Kinesis Data Streams
            Real-time data ingestion
            Custom processing
            Shards for scaling
            Retain: 1-365 days
            Producers & Consumers
        Kinesis Data Firehose
            Load streaming data
            Near real-time
            No management
            Transform with Lambda
            Destinations: S3, Redshift, OpenSearch
        Kinesis Data Analytics
            SQL on streaming data
            Apache Flink
            Real-time analytics
            No servers to manage
        Kinesis Video Streams
            Stream video
            WebRTC
            ML processing
            Video playback
```

### Kinesis Data Streams Architecture

```mermaid
graph LR
    subgraph Producers_Group["Producers"[
        App["Applications&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Kinesis Producer Library"[
        Agent["Kinesis Agent&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Log files"[
        SDK["AWS SDK&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;PutRecord API"[
        IoT[IoT Devices[
    end
    
    subgraph Kinesis_Data_Stream_Group["Kinesis Data Stream"[
        Stream["Kinesis Data Stream&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;my-stream"[
        
        Shard1["Shard 1&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;1 MB/s in&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;2 MB/s out"[
        Shard2["Shard 2&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;1 MB/s in&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;2 MB/s out"[
        Shard3["Shard 3&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;1 MB/s in&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;2 MB/s out"[
        
        Stream --> Shard1
        Stream --> Shard2
        Stream --> Shard3
    end
    
    subgraph Consumers_Group["Consumers"[
        Lambda["Lambda&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Event processing"[
        EC2["EC2/ECS&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Kinesis Client Library"[
        Firehose["Kinesis Firehose&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Load to S3/Redshift"[
        Analytics["Kinesis Analytics&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;SQL queries"[
    end
    
    App --> Shard1
    Agent --> Shard2
    SDK --> Shard3
    IoT --> Shard1
    
    Shard1 --> Lambda
    Shard2 --> EC2
    Shard3 --> Firehose
    Shard1 --> Analytics
    
    Features["Features:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Real-time 70ms-200ms&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Replay capability&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Retention: 1-365 days&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Immutable records&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Ordered per shard&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;💰 Pay per shard-hour + PUT"[
    
    classDef style1 fill:#FF9900
    class Stream style1
    classDef style2 fill:#569A31
    class Shard1 style2
```

### Kinesis Data Firehose

```mermaid
graph TB
    subgraph Data_Sources_Group["Data Sources"[
        DirectPut["Direct PUT&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Applications, SDK"[
        KinesisStreams[Kinesis Data Streams[
        CloudWatch[CloudWatch Logs[
        IoTCore[AWS IoT[
    end
    
    subgraph Kinesis_Firehose_Group["Kinesis Firehose"[
        Firehose["Kinesis Data Firehose&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Fully managed&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Auto-scaling&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Near real-time"[
        
        Transform["Optional Transformation&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Lambda function&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Convert, enrich, filter"[
        
        Batch["Batching&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Buffer: 1 MB - 128 MB&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Interval: 60s - 900s"[
        
        Firehose --> Transform
        Transform --> Batch
    end
    
    subgraph Destinations_Group["Destinations"[
        S3["Amazon S3&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Data lake&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Parquet, ORC, JSON"[
        
        Redshift["Amazon Redshift&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Copy via S3"[
        
        OpenSearch["Amazon OpenSearch&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Log analytics"[
        
        Splunk["Splunk&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;3rd party"[
        
        HTTP["Custom HTTP Endpoint&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Datadog, New Relic"[
    end
    
    subgraph Backup_Group["Backup"[
        BackupS3["Backup S3 Bucket&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;All source records&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Failed records"[
    end
    
    DirectPut --> Firehose
    KinesisStreams --> Firehose
    CloudWatch --> Firehose
    IoTCore --> Firehose
    
    Batch --> S3
    Batch --> Redshift
    Batch --> OpenSearch
    Batch --> Splunk
    Batch --> HTTP
    
    Firehose -.Optional.-> BackupS3
    
    VsStreams["Firehose vs Data Streams:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Firehose: Fully managed, near real-time, destinations&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Streams: Real-time, custom processing, replay"[
    
    classDef style1 fill:#FF9900
    class Firehose style1
    classDef style2 fill:#569A31
    class S3 style2
```

### Kinesis Data Analytics

```mermaid
graph TB
    subgraph Input_Streams_Group["Input Streams"[
        KinesisIn["Kinesis Data Streams&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Real-time input"[
        FirehoseIn["Kinesis Firehose&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Near real-time input"[
        S3Reference["S3 Reference Data&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Enrich streaming data"[
    end
    
    subgraph Kinesis_Data_Analytics_Group["Kinesis Data Analytics"[
        Analytics[Kinesis Data Analytics[
        
        SQL["SQL Application&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Standard SQL queries&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Windowing, aggregations"[
        
        Flink["Apache Flink Application&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Java, Scala, Python&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Advanced processing"[
        
        Analytics --> SQL
        Analytics --> Flink
    end
    
    subgraph Output_Destinations_Group["Output Destinations"[
        KinesisOut["Kinesis Data Streams&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Further processing"[
        FirehoseOut["Kinesis Firehose&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Load to destinations"[
        Lambda["Lambda&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Custom processing"[
    end
    
    KinesisIn --> SQL
    FirehoseIn --> SQL
    S3Reference -.Enrich.-> SQL
    
    KinesisIn --> Flink
    
    SQL --> KinesisOut
    SQL --> FirehoseOut
    SQL --> Lambda
    
    Flink --> KinesisOut
    Flink --> FirehoseOut
    
    UseCases["Use Cases:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Real-time dashboards&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Real-time metrics&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Streaming ETL&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Anomaly detection&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• IoT analytics"[
    
    Features["Features:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Serverless&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Auto-scaling&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Pay for processing&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ IAM for access control&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Schema discovery"[
    
    classDef style1 fill:#FF9900
    class Analytics style1
    classDef style2 fill:#569A31
    class SQL style2
```

## AWS Glue

### Glue ETL Architecture

```mermaid
graph TB
    subgraph Data_Sources_Group["Data Sources"[
        S3_Source[S3 Data Lake[
        RDS_Source[RDS Databases[
        DynamoDB_Source[DynamoDB[
        JDBC_Source["JDBC Sources&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;On-premises DBs"[
    end
    
    subgraph AWS_Glue_Group["AWS Glue"[
        Crawler["Glue Crawler&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Auto-discover schema&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Populate catalog"[
        
        Catalog["Glue Data Catalog&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Central metadata repository&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Table definitions&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Schema versions"[
        
        ETL["Glue ETL Jobs&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Serverless Spark/Python&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Transform data&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Auto-scaling"[
        
        Scheduler["Job Scheduler&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Time-based triggers&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Event-based triggers"[
        
        Crawler --> Catalog
        Catalog --> ETL
        Scheduler --> ETL
    end
    
    subgraph Data_Targets_Group["Data Targets"[
        S3_Target["S3 Data Lake&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Parquet, ORC, CSV"[
        Redshift_Target["Redshift&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Data warehouse"[
        RDS_Target["RDS/Aurora&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Analytics DB"[
    end
    
    S3_Source --> Crawler
    RDS_Source --> Crawler
    DynamoDB_Source --> Crawler
    JDBC_Source --> Crawler
    
    ETL --> S3_Target
    ETL --> Redshift_Target
    ETL --> RDS_Target
    
    Athena[Amazon Athena[ -.Query.-> Catalog
    EMR[Amazon EMR[ -.Use.-> Catalog
    Redshift2[Redshift Spectrum[ -.Use.-> Catalog
    
    Features["Features:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Serverless&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Pay per second for ETL&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Python or Scala&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Built-in transformations&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Job bookmarks&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Development endpoints"[
    
    classDef style1 fill:#FF9900
    class Catalog style1
    classDef style2 fill:#569A31
    class ETL style2
```

### Glue Data Catalog

```mermaid
graph TB
    subgraph Data_Catalog_Components_Group["Data Catalog Components"[
        Catalog["Glue Data Catalog&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Metadata repository"[
        
        Database["Databases&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Logical grouping"[
        
        Tables["Tables&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Schema definition&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Column types&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Partitions"[
        
        Crawler_Config["Crawlers&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Scan data sources&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Infer schema"[
        
        Catalog --> Database
        Database --> Tables
        Catalog --> Crawler_Config
    end
    
    subgraph Services_Using_Catalog_Group["Services Using Catalog"[
        Athena["Amazon Athena&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;SQL queries"[
        
        Redshift_Spectrum["Redshift Spectrum&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Query S3"[
        
        EMR["Amazon EMR&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Spark, Hive"[
        
        Glue_ETL["Glue ETL Jobs&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Transform data"[
    end
    
    Tables --> Athena
    Tables --> Redshift_Spectrum
    Tables --> EMR
    Tables --> Glue_ETL
    
    Benefits["Benefits:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Single source of truth&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Avoid data silos&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Schema evolution&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Partition discovery&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Cross-service metadata&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;💰 First million objects stored free"[
    
    Hive["Hive Metastore Compatible&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Import existing Hive catalogs"[ -.Compatible.-> Catalog
    
    classDef style1 fill:#FF9900
    class Catalog style1
    classDef style2 fill:#569A31
    class Tables style2
```

## Amazon QuickSight

### QuickSight Architecture

```mermaid
graph TB
    subgraph Data_Sources_Group["Data Sources"[
        RDS["RDS/Aurora"[
        Redshift[Redshift[
        Athena[Athena[
        S3[S3[
        Salesforce[Salesforce[
        Excel[Excel, CSV[
        OnPrem["On-Premises DBs&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;via VPC"[
    end
    
    subgraph QuickSight_Group["QuickSight"[
        SPICE["SPICE In-Memory Engine&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Super-fast Performance&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Interactive Caching Engine&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Columnar storage"[
        
        Datasets["Datasets&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Data preparation&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Joins, filters, transforms"[
        
        Analysis["Analysis&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Visual exploration&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Drag-and-drop"[
        
        Dashboards["Dashboards&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Published views&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Share with users"[
        
        Datasets --> SPICE
        SPICE --> Analysis
        Analysis --> Dashboards
    end
    
    subgraph Features_Group["Features"[
        ML["QuickSight ML Insights&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Anomaly detection&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Forecasting&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Natural language queries"[
        
        Embedded["Embedded Analytics&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Embed in applications&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Custom branding"[
        
        Enterprise["Enterprise Edition&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Row-level security&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;AD integration&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Encryption at rest"[
    end
    
    RDS --> Datasets
    Redshift --> Datasets
    Athena --> Datasets
    S3 --> Datasets
    Salesforce --> Datasets
    Excel --> Datasets
    OnPrem --> Datasets
    
    Dashboards --> ML
    Dashboards --> Embedded
    Dashboards --> Enterprise
    
    Pricing["Pricing:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;💰 Standard: $9/user/month&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;💰 Enterprise: $18/user/month&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;💰 SPICE: $0.25/GB/month&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;💰 Readers: $0.30/session $5 max"[
    
    classDef style1 fill:#FF9900
    class SPICE style1
    classDef style2 fill:#569A31
    class Dashboards style2
```

## Amazon OpenSearch (ElasticSearch)

### OpenSearch Architecture

```mermaid
graph TB
    subgraph Data_Ingestion_Group["Data Ingestion"[
        Kinesis["Kinesis Firehose&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Streaming logs"[
        Logstash["Logstash&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Log shipping"[
        CloudWatch[CloudWatch Logs[
        Lambda[Lambda Functions[
        IoT[AWS IoT[
    end
    
    subgraph OpenSearch_Domain_Group["OpenSearch Domain"[
        Master["Master Nodes&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Cluster management&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Optional, dedicated"[
        
        Data1["Data Node 1&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Store & search&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Instance types"[
        Data2["Data Node 2&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Store & search"[
        Data3["Data Node 3&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Store & search"[
        
        UltraWarm["UltraWarm Nodes&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Read-only&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;S3-backed&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Cost-effective"[
        
        ColdStorage["Cold Storage&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;S3-based&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Infrequent access&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Lowest cost"[
        
        Master --> Data1
        Master --> Data2
        Master --> Data3
        
        Data1 --> UltraWarm
        UltraWarm --> ColdStorage
    end
    
    subgraph Access_Visualization_Group["Access & Visualization"[
        Kibana["OpenSearch Dashboards&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Formerly Kibana&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Visualization"[
        
        API["REST API&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Search queries&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;CRUD operations"[
        
        SQL["SQL Support&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Query with SQL&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;JDBC driver"[
    end
    
    Kinesis --> Data1
    Logstash --> Data2
    CloudWatch --> Data3
    Lambda --> Data1
    IoT --> Data2
    
    Data1 --> Kibana
    Data1 --> API
    Data1 --> SQL
    
    Features["Features:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Multi-AZ deployment&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Built-in dashboards&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Full-text search&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Application monitoring&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;✅ Log analytics&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;💰 Pay per instance hour"[
    
    UseCases["Use Cases:&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Log analytics&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Application monitoring&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Security analytics&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Full-text search&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;• Clickstream analytics"[
    
    classDef style1 fill:#FF9900
    class Master style1
    classDef style2 fill:#569A31
    class Data1 style2
    classDef style3 fill:#146EB4
    class Kibana style3
```

## Analytics Architecture Patterns

### Real-Time Analytics Pipeline

```mermaid
graph LR
    subgraph Data_Sources_Group["Data Sources"[
        Website[Website Clickstream[
        Mobile[Mobile App Events[
        IoT[IoT Sensors[
    end
    
    subgraph Real_Time_Ingestion_Group["Real-Time Ingestion"[
        Kinesis["Kinesis Data Streams&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Real-time collection"[
    end
    
    subgraph Stream_Processing_Group["Stream Processing"[
        Lambda["Lambda&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Transform"[
        Analytics["Kinesis Analytics&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Windowing, aggregation"[
    end
    
    subgraph Storage_Analysis_Group["Storage & Analysis"[
        Firehose[Kinesis Firehose[
        S3["S3 Data Lake&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Parquet format"[
        OpenSearch["OpenSearch&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Real-time dashboards"[
    end
    
    subgraph Batch_Analysis_Group["Batch Analysis"[
        Glue["Glue ETL&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Nightly processing"[
        Athena["Athena&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Ad-hoc queries"[
        Redshift["Redshift&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Data warehouse"[
    end
    
    subgraph Visualization_Group["Visualization"[
        QuickSight["QuickSight&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;BI dashboards"[
        Kibana["OpenSearch Dashboards&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Real-time monitoring"[
    end
    
    Website --> Kinesis
    Mobile --> Kinesis
    IoT --> Kinesis
    
    Kinesis --> Lambda
    Kinesis --> Analytics
    
    Lambda --> Firehose
    Analytics --> Firehose
    
    Firehose --> S3
    Firehose --> OpenSearch
    
    S3 --> Glue
    Glue --> Redshift
    S3 --> Athena
    
    Redshift --> QuickSight
    Athena --> QuickSight
    OpenSearch --> Kibana
    
    classDef style1 fill:#FF9900
    class Kinesis style1
    classDef style2 fill:#569A31
    class S3 style2
    classDef style3 fill:#146EB4
    class QuickSight style3
```

### Batch Analytics Pipeline

```mermaid
graph TB
    subgraph Data_Sources_Group["Data Sources"[
        Databases["RDS/Aurora&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Transactional DBs"[
        Apps["Application Logs&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;S3 buckets"[
        OnPrem["On-Premises&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;DataSync"[
    end
    
    subgraph Data_Lake_S3_Group["Data Lake - S3"[
        Raw["Raw Zone&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Original data&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;All formats"[
        
        Processed["Processed Zone&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Cleaned data&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Parquet/ORC"[
        
        Curated["Curated Zone&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Business views&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Aggregated"[
    end
    
    subgraph ETL_Processing_Group["ETL Processing"[
        Glue["AWS Glue&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Serverless ETL&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Scheduled jobs"[
        
        EMR["Amazon EMR&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Complex transformations&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Spark jobs"[
    end
    
    subgraph Data_Catalog_Group["Data Catalog"[
        Catalog["Glue Data Catalog&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Metadata&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Schema registry"[
    end
    
    subgraph Analytics_Group["Analytics"[
        Athena["Athena&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;SQL queries&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Interactive"[
        
        Redshift["Redshift&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Data warehouse&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;OLAP"[
        
        SageMaker["SageMaker&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;ML training"[
    end
    
    Databases --> Raw
    Apps --> Raw
    OnPrem --> Raw
    
    Raw --> Glue
    Glue --> Processed
    Glue --> Catalog
    
    Processed --> EMR
    EMR --> Curated
    EMR --> Catalog
    
    Catalog --> Athena
    Catalog --> Redshift
    
    Curated --> Athena
    Curated --> Redshift
    Curated --> SageMaker
    
    Athena --> QuickSight["QuickSight&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;Dashboards"[
    Redshift --> QuickSight
    
    classDef style1 fill:#C00
    class Raw style1
    classDef style2 fill:#FF9900
    class Processed style2
    classDef style3 fill:#569A31
    class Curated style3
```

