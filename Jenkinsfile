pipeline {
  agent any
  options { timeout(time: 120, unit: 'SECONDS') } //
  environment {
    REPO = 'https://gitee.com/hanzhichao/api-auto.git'
  }
// there's bug when use parameters "sh: sh: command not found"
//   parameters {
//     string(name: 'path', defaultValue: 'testcases', description: '指定要执行的用例或用例目录，多个以空格隔开。')
//     choice(name: 'mark',
//            choices: ['','smoke', 'scene', 'abnormal', 'ddt', 'hzc', 'jw'],
//            description: '选择运行带指定标记的用例。')
//   }
  stages {
//     stage('拉取代码') {
//       steps {
//         git "${env.REPO}"
//       }
//     }
    stage('执行用例') {
//       when { environment name: 'mark', value: '' }
      steps {
//         sh "python3 -m pytest ${params.path}"
        sh "python3 -m pytest testcases"
      }
    }
//     stage('执行指定标记用例') {
//       when { not { environment name: 'mark', value: '' } }
//       steps {
//         sh "python3 -m pytest ${params.path} -m ${params.mark}"
//       }
//     }
  }
  post {
    always {
        allure includeProperties: false, jdk: '', results: [[path: 'reports/allure_data']]
        mail to: 'ivan@163.com,superhin@126.com', from: 'test_results@sina.com', bcc: '', cc: '', replyTo: '',
            subject: '[CRM]接口测试报告',
            mimeType: 'text/html', charset: 'utf-8',
            body: '''<h3>Hi, All</h3>
    接口自动化测试执行完成，点击以下链接查看在下Allure测试报告：<br/>
    <a href="http://localhost:8080/job/apitest/allure/">http://localhost:8080/job/apitest/allure/</a> <br/>
    附件中为HTML测试报告及Jenkins构建日志'''
    }
  }
}
