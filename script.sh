# clone the repo for running evaluation
git clone https://github.com/AI4Bharat/indicTrans.git
cd indicTrans
# clone requirements repositories
git clone https://github.com/anoopkunchukuttan/indic_nlp_library.git
git clone https://github.com/anoopkunchukuttan/indic_nlp_resources.git
git clone https://github.com/rsennrich/subword-nmt.git
cd ..


pip install sacremoses pandas mock sacrebleu tensorboardX pyarrow indic-nlp-library --user 
pip install mosestokenizer subword-nmt --user
# Install fairseq from source
git clone https://github.com/pytorch/fairseq.git
cd fairseq
# !git checkout da9eaba12d82b9bfc1442f0e2c6fc1b895f4d35d
pip install ./ --user
pip install xformers --user
cd ..

curl -O https://ai4b-public-nlu-nlg.objectstore.e2enetworks.net/indic2en.zip
unzip indic2en.zip