<p align="center">
  <img src="assets/nids-banner.png" alt="Machine Learning Network Intrusion Detection System" width="100%">
</p>
# ML-Network-Intrusion-Detection

Machine Learning-based Network Intrusion Detection System.
<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-AI-green?logo=scikitlearn)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-NIDS-red)
![Status](https://img.shields.io/badge/Project-Research%20Prototype-orange)

</p>
---

## 📌 Project Overview

The **Machine Learning-Based Network Intrusion Detection System (NIDS)** is an Artificial Intelligence-driven cybersecurity research project designed to identify malicious network activities and distinguish them from legitimate traffic.

The system analyzes network flow characteristics using machine learning algorithms to detect and classify different categories of cyber threats. The project explores the application of AI techniques for automated threat intelligence, anomaly detection, and network security monitoring.

---

## 🎯 Objectives

- Develop an ML-based framework for automated network intrusion detection.
- Analyze network traffic features to identify abnormal communication patterns.
- Classify network activities into normal and malicious categories.
- Evaluate machine learning models using standard performance metrics.
- Explore AI-based approaches for improving cybersecurity defense mechanisms.

---

## 📌 Architecture Diagram

![NIDS Architecture](assets/nids-architecture.png)

---

## 🧠 ML Workflow Visualization

![ML Workflow](assets/nids-ml-workflow.png)


\## **Technologies Used**



\* Python

\* Pandas

\* NumPy

\* Scikit-Learn

\* Matplotlib

\* Jupyter Notebook



\## **Project Structure**



data/ - Datasets



notebooks/ - Experiments and analysis



src/ - Source code



models/ - Trained models



results/ - Evaluation reports and visualisations



\## **Status**



Project initialised and repository structure created.



\## **Future Work**



\* Dataset preprocessing

\* Feature engineering

\* Model training

\* Performance evaluation

\* Real-time intrusion detection

## **Dataset Information**



This project uses the NSL-KDD dataset, a benchmark dataset for Network Intrusion Detection Systems (NIDS).



**Dataset Files:**

\- KDDTrain+.txt : Training dataset

\- KDDTest+.txt : Testing dataset



The dataset contains normal network traffic and multiple categories of cyberattacks, including:



\- Denial of Service (DoS)

\- Probe Attacks

\- Remote to Local (R2L)

\- User to Root (U2R)



**Dataset Location:**



data/

├── KDDTrain+.txt

└── KDDTest+.txt

## **Project Architecture**



```text

Network Traffic

&#x20;      │

&#x20;      ▼

+------------------+

|  NSL-KDD Dataset |

+------------------+

&#x20;      │

&#x20;      ▼

+------------------+

| Data Preprocessing |

+------------------+

&#x20;      │

&#x20;      ▼

+------------------+

| Feature Selection |

+------------------+

&#x20;      │

&#x20;      ▼

+------------------+

| ML Model Training |

| (Random Forest)  |

+------------------+

&#x20;      │

&#x20;      ▼

+------------------+

| Attack Detection |

+------------------+

&#x20;      │

&#x20;      ▼

+------------------+

| Performance Evaluation |

+------------------+

```

