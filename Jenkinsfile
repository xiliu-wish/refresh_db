@Library('pipeline@master') _
pipeline {
    agent {
      label "wishpost-test"
    }
    parameters {
        booleanParam(name: 'wishpost',defaultValue: true, description:'update pg')
    }
    // before the stages running, the agent should installed mongo and pg client
    stages {
        stage("update pg from snapshot"){
            steps {
                script {
                    if (params.wishpost){
                        sh """
                        mv .pg_service.conf ~/.
                        echo "pg is updating"
                        export PGSERVICE=snapshot
                        psql -d postgres -tc "SELECT 1 FROM pg_database WHERE datname = 'qa'" | grep -q 1 || psql -d postgres -c "CREATE DATABASE qa"
                        pg_dump -s > schema.sql prod
                        psql -d qa < schema.sql
                        pg_dump -a -t payment_account -t payment_user -t remark_keys > data.sql prod
                        psql -d qa < data.sql
                        rm -rf schema.sql data.sql
                        """
                    }
                }
            }
        }
    }
}