<p align="center">
  <img src="assets/nids-banner.png" alt="Machine Learning Network Intrusion Detection System" width="100%">
</p>
# ML-Network-Intrusion-Detection

Machine Learning-based Network Intrusion Detection System.




\## **Project Overview**



This project aims to develop a Machine Learning-based Network Intrusion Detection System (NIDS) capable of identifying malicious network traffic and distinguishing it from normal network activity.



The system will use machine learning algorithms to analyze network flow features and classify different types of cyberattacks.



\## **Objectives**



\* Detect malicious network activity.

\* Classify network traffic as normal or attack.

\* Compare the performance of multiple machine learning models.

\* Improve cybersecurity monitoring through automated threat detection.



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

