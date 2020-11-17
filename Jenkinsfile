@Library('pipeline@master') _
pipeline {
    agent {
      label "build"
    }
    parameters {
        string(name: 'wishpost_mongo_snapshot_ip', defaultValue: '10.88.50.219', description: 'wishpost mongo snapshot host')
        string(name: 'wishpost_pg_host', defaultValue: 'wishpost-snapshot-2020-11-13-07-41.cvhxilsgfnbf.rds.cn-north-1.amazonaws.com.cn', description: 'wishpost pg snapshot host')
        string(name: 'wishwms_mongo_snapshot_ip', defaultValue: '....', description: 'wishwms mongo snapshot host')

    }
    // before the stages running, the agent should installed mongo and pg client
    stages {
        stage("update mongo from snapshot"){
            steps {
                script {
                    if (params.wishpost) {
                        sh """
                        echo "wishpost need to be updated"
                        echo "execute mongo update"
                        """

                        sh """
                        echo "wishpost pg need to be updated"
                        echo "execute pg update end"
                        """
                    }else{
                        sh """ echo "wishpost" """
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