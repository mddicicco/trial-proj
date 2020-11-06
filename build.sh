openssl aes-256-cbc -K $encrypted_06826a922d57_key -iv $encrypted_06826a922d57_iv -in travis.pem.enc -out travis.pem -d
chmod 400 travis.pem
ssh -i travis.pem -L 6500:saitama.cluster-c0u7eogrlc5a.us-east-2.rds.amazonaws.com:3306 travis@3.128.201.81 &