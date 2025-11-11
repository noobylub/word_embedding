# Word Embedding Model: FastText

This project implements word embedding models for Indonesian and Malaysian text using FastText. Indonesian is a language with very rich morphology, making it an interesting case for word embedding research.

## Prerequisites

Before cloning this repository, you **must** have Git LFS (Large File Storage) installed, as this project contains large text datasets tracked by LFS.

### Install Git LFS

**macOS:**
```bash
brew install git-lfs
```

**Linux:**
```bash
sudo apt-get install git-lfs  # Ubuntu/Debian
# or
sudo yum install git-lfs      # CentOS/RHEL
```

**Windows:**
Download and install from [git-lfs.github.com](https://git-lfs.github.com/)

After installation, run:
```bash
git lfs install
```

## Setup Instructions

Follow these steps to set up the project:

### 1. Clone this repository
```bash
git clone https://github.com/noobylub/word_embedding.git
cd word_embedding
```

**Note:** Git LFS will automatically download the large files during cloning. If you see pointer files instead of actual data, run:
```bash
git lfs pull
```

### 2. Set up a virtual environment
```bash
python -m venv wordembedding_env
source wordembedding_env/bin/activate  # macOS/Linux
# wordembedding_env\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start Jupyter Notebook
```bash
jupyter notebook
```

### 5. Open the notebooks
- `preprocess_malaysian.ipynb` - Malaysian text preprocessing
- `indonesian_text_process.ipynb` - Indonesian text processing
- Run cells sequentially or use "Cell" → "Run All"

## Project Structure

```
word_embedding/
├── indonesian_text/          # Indonesian text datasets (LFS tracked)
│   ├── news_content.txt
│   └── news_text.txt
├── malaysian_text/            # Malaysian text datasets (LFS tracked)
│   └── malay_shahbudin.txt
├── dirty_indonesian_text/     # Raw Indonesian data (LFS tracked)
│   ├── indTweets.csv
│   └── news_dataset.csv
├── dirty_malaysian_text/      # Raw Malaysian data (LFS tracked)
│   └── shahbudindotcom.net.jsonl
├── preprocess_malaysian.ipynb # Malaysian preprocessing notebook
├── indonesian_text_process.ipynb # Indonesian processing notebook
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Large Files (Git LFS)

This repository uses Git LFS to manage large text datasets. The following directories contain files tracked by LFS:
- `indonesian_text/**` - ~218 MB
- `malaysian_text/**` - ~217 MB
- `dirty_indonesian_text/**` - ~218 MB
- `dirty_malaysian_text/**` - ~163 MB

**Total LFS storage:** ~816 MB

If you encounter issues with LFS files, verify they were downloaded correctly:
```bash
git lfs ls-files  # List all LFS-tracked files
git lfs pull      # Download LFS files if needed
```

## Dependencies

The main dependencies are listed in `requirements.txt` and include:
- jupyter
- pandas
- numpy
- fasttext (for word embeddings)
- scikit-learn
- matplotlib

Install all dependencies at once with:
```bash
pip install -r requirements.txt
```

## Contributing

When contributing to this repository:
1. Ensure Git LFS is installed and initialized
2. Large data files will automatically be tracked by LFS (see `.gitattributes`)
3. Follow the existing code structure and documentation style

## Troubleshooting

**Problem:** Files appear as small pointer files instead of actual data  
**Solution:** Run `git lfs pull` to download the actual files

**Problem:** `git push` fails with large files  
**Solution:** Ensure Git LFS is installed and run `git lfs install`

**Problem:** Out of LFS bandwidth  
**Solution:** GitHub free accounts have 1GB/month LFS bandwidth. Consider upgrading or waiting for the monthly reset.