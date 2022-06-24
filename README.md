```
$ docker-compose up -d
$ docker-compose exec rpm bash

# cd /app
# rm -rf /app/rpmbuild
# rpmbuild -ba dateoutput.spec
# cp -r ~/rpmbuild /app
```
