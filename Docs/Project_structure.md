# RCAR Streamlit PoC - Project structure
### Table of content

- [(Root)](#root)
- [Airflow pipeline](#airflow-pipeline-airflow_pipeline)
- [Streamlit Modular package RCAR-OCR](#streamlit-modular-package-rcar-ocr-streamlit_app)

This markdown document contains full description of the project's structure. The first section contains a holistic view of the project's modules followed by other sections that describes each module (project folders). Each section contains the directory tree, description of each folder/file, tree level and the count of folders and files.

###  (Root)

    .
    ├── airflow_pipeline/               #1
    ├── data/                           #2
    ├── Docs/                           #3 
    ├── ocr_preprocessing/              #4
    ├── openai_local/                   #5
    ├── streamlit_app/                  #6
    ├── string_similarity_utils/        #7
    ├── tessdata/                       #8
    ├── textify_docs/                   #9
    ├── compose.yaml                    #10
    ├── config.py                       #11
    ├── config.yaml                     #12
    ├── constants.py                    #13
    ├── Dockerfile                      #14
    ├── main.py                         #15
    ├── paths.py                        #16
    ├── README.md                       #17
    ├── requirements.txt                #18
    └── utils.py                        #19
    
    Tree level: 0
    Folders: 9 | Files: 9 (Not including hidden ones)

**Description**
1. Automation pipeline
2. Input/Output data
3. Project documentaion 
4. Contains methods for preprocessing images/pdfs
5. Contains methods for handling requests to OpenAI API
6. Streamlit Web App
7. String similarity tools
8. Contains tesseract data
9. Contains all methods for OCR operations (Converting img/pdf to text)
10. Docker Compose file
11. Script for loading configuration from yaml
12. Yaml file that contain the configuration of project
13. Contain constant variables
14. Docker file
15. Project's main script (Launching script)
16. Paths of directories
17. Getting started document
18. Required python packages
19. Contain methods for processing img/pdfs

### Airflow pipeline (airflow_pipeline)

    .
    ├── config/                                                 #1
    │   ├── config.py                                   #1-1
    │   └── config.yml                                  #1-2
    ├── main.py                                                 #2
    ├── paths.py                                                #3
    ├── tasks/                                                  #4
    │   ├── step01_save_pdf_and_convert_to_images.py    #4-1
    │   ├── step02_enhance_images.py                    #4-2
    │   ├── step03_crop_images.py                       #4-3
    │   ├── step04_detect_tables.py                     #4-4
    │   ├── step05_merge_tables.py                      #4-5
    │   ├── step06_extract_text.py                      #4-6
    │   ├── step07_extract_fields_using_llm.py          #4-7
    │   ├── step07_save_text.py                         #4-8
    │   ├── step08_export_data.py                       #4-9
    │   └── task_decorator.py                           #4-10
    └── utils.py                                                #5

    Tree level: 1
    Folders: 2 | Files: 15

**Description** \

### Streamlit Modular package RCAR-OCR (streamlit_app)

    .
    ├── tests/                          #1
    ├── .gitlab-ci.yml                  #2
    ├── app_constants.py                #3
    ├── app_css.py                      #4
    ├── app.py                          #5
    ├── config.yaml                     #6
    └── Dockerfile                      #7
    
    Tree level: 0
    Folders: 1 | Files: 6

**Description**
1. Test directory (if necessary)
2. Gitlab CI/CD pipeline definition
3. Contain constant variables
4. Contain CSS styling
5. The Streamlit application
6. Yaml file that contain the configuration of Streamlit App
7. Docker file