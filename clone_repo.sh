git clone https://github.com/zadam/trilium/ trilium/
cd trilium
# checkout to the latest version
git checkout $(git describe --tags $(git rev-list --tags --max-count=1))

cd ..
mv -f trilium/* ./