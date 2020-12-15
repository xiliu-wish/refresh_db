@Library('pipeline@master') _
pipeline {
    agent {
      label "wishpost-test"
    }
    parameters {
        string(name: 'wishpost_mongo_snapshot_ip', defaultValue: '10.88.50.10', description: 'wishpost mongo snapshot host')
        string(name: 'wishpost_mongo_qa_ip', defaultValue: '10.88.51.219', description: 'wishpost mongo qa host')
        booleanParam(name: 'is_dump',defaultValue: true, description:'dump data')
        booleanParam(name: 'is_restore',defaultValue: true, description:'restore data to QA')


    }
    // before the stages running, the agent should installed mongo and pg client
    stages {
        stage("back up the key collection"){
            steps {
                script{
                    println("backup important collection of QA")
                    sh '''
                    sudo rm -rf backup
                    for c in `cat wishpost/keep_wishpost_tables.txt`; do sudo mongodump --host ''' + params.wishpost_mongo_qa_ip + ''' -d wishpost -c ${c}  -o ./backup ; done
                    for c in `cat wishpost/keep_sweeper_tables.txt`; do sudo mongodump --host ''' + params.wishpost_mongo_qa_ip + ''' -d sweeper -c ${c}  -o ./backup ; done
                    '''
                }
            }
        }
        stage("dump data from snapshot"){
            steps {
                script {
                    if(params.is_dump){
                        println("wishpost need to be updated")
                        println("update wishpost mongo: db is wishpost")
                        sh '''
                        sudo rm -rf dump
                        for c in `cat wishpost/wishpost_select_tables.txt`; do sudo mongodump --host ''' + params.wishpost_mongo_snapshot_ip + ''' -d wishpost -c ${c}  -o ./dump ; done
                        for c in `cat wishpost/sweeper_select_tables.txt`; do sudo mongodump --host ''' + params.wishpost_mongo_snapshot_ip + ''' -d sweeper -c ${c}  -o ./dump ; done
                        '''
                    }
                }
            }
        }
        stage("restore data to QA"){
            steps {
                script {
                    if (params.is_restore){
                        sh """
                        sudo mongorestore -d wishpost -h ${params.wishpost_mongo_qa_ip} --drop --dir=dump/wishpost
                        sudo mongorestore -d sweeper -h ${params.wishpost_mongo_qa_ip} --drop --dir=dump/sweeper
                        """
                    }
                }
            }
        }
        stage("warm up"){
            steps {
                script {
                    println("To warm up, you need go to wishpost-be-qa ec2, and execute the following command")
                    println(                        
                    """
                    sudo -i
                    export AWS_CONFIG_FILE=/etc/boto.cfg 
                    export PYTHONPATH=/production/wishpost/current
                    /production/wishpost/persistent/virtualenv/bin/python /production/wishpost/current/wishpost/micro/payment_pricing/scripts/warmup_pricing_cache.py --env=be_qa --back_days=-1 --forward_days=-1 --job_name="warm up"
                    """
                    )
                }
            }
        }
    }
}