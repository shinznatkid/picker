# Fabric v1

from fabric.api import local


def upload():
    try:
        local('rm -r ./dist')
    except:
        pass
    local('python setup.py sdist bdist_wheel')
    local('twine upload dist/*')  # optional args  --repository your-repo-name or --repository-url https://upload.pypi.org/legacy/
