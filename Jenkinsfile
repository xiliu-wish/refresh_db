@Library('pipeline@master') _
pipeline {
    agent {
      label "build"
    }
    parameters {
        string(name: 'wishpost_mongo_snapshot_ip', defaultValue: '10.88.50.10', description: 'wishpost mongo snapshot host')
        string(name: 'wishpost_pg_host', defaultValue: 'wishpost-snapshot-2020-11-13-07-41.cvhxilsgfnbf.rds.cn-north-1.amazonaws.com.cn', description: 'wishpost pg snapshot host')
        string(name: 'wishpost_mongo_qa_host', defaultValue: '10.88.51.219', description: 'wishpost mongo qa host')
        string(name: 'wishwms_mongo_snapshot_ip', defaultValue: '....', description: 'wishwms mongo snapshot host')
    }
    // before the stages running, the agent should installed mongo and pg client
    stages {
        stage("update wishpost mongo from snapshot"){
            steps {
                script {
                    println("test")
                    if (params.wishpost) {
                        println("wishpost need to be updated")
                        println("update wishpost mongo: db is wishpost")
                        sh '''
                        for c in `cat ./sweeper_tables.txt`; do mongodump --host ${params.wishpost_mongo_snapshot_ip} -d wishpost -c $c  -o ./dump ; done
                        '''
                        sh """
                        mongorestore -h ${wishpost_mongo_qa_host} -d sweeper --drop --dir=dump/sweeper
                        """
                        sh '''
                        for c in `cat ./wishpost_tables.txt`; do mongodump --host ${params.wishpost_mongo_snapshot_ip} -d wishpost -c $c  -o ./dump ; done
                        '''
                        sh """
                        mongorestore -h ${wishpost_mongo_qa_host} -d sweeper --drop --dir=dump/sweeper
                        """
                    }else{
                        print("wishpost doesn't need to be updated")
                    }
                }
            }
        }
        stage("update pg from snapshot"){
            steps {
                script {
                    if (params.wishwms){
                    sh """
                    echo "wishwms mongo need to be updated"
                    echo "execute pg update "
                    """
                    }
                }
            }
        }
    }
}