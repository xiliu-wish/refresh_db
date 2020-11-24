@Library('pipeline@master') _
pipeline {
    agent {
      label "wishpost-test"
    }
    parameters {
        string(name: 'wishpost_mongo_snapshot_ip', defaultValue: '10.88.50.10', description: 'wishpost mongo snapshot host')
        string(name: 'wishpost_mongo_qa_ip', defaultValue: '10.88.51.219', description: 'wishpost mongo qa host')
    }
    // before the stages running, the agent should installed mongo and pg client
    stages {
        stage("update wishpost mongo from snapshot"){
            steps {
                script {
                    println("test")
                    println("wishpost need to be updated")
                    println("update wishpost mongo: db is wishpost")
                    sh '''
                    for c in `cat wishpost/wishpost_select_tables.txt`; do sudo mongodump --host ''' + params.wishpost_mongo_snapshot_ip + ''' -d wishpost -c ${c}  -o ./dump ; done
                    '''
                    sh """sudo mongorestore -d wishpost -h ${params.wishpost_mongo_qa_host} --drop --dir=dump/wishpost"""
                    
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