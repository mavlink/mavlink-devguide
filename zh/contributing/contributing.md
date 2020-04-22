# 为 mavlink 做贡献

We follow the [Github flow](https://guides.github.com/introduction/flow/) development model.

Contributions are divided into several categories:

* Complicated changes that require significant review should be initiated using an RFC pull request in [mavlink/rfcs](https://github.com/mavlink/rfcs). This is primarily intended for new microservice interface definitions, as these require discussion of both messages and message sequences (state machines) \(examples: parameter or mission protocol\). Depending on the scope of the change, it may also be required when *modifying* a microservice.
* Less complex changes should be submitted as a PRs to the [mavlink/mavlink](https://github.com/mavlink/mavlink) repository. This includes message additions/changes that do not affect a state machine.
* Changes to mavgen generator code should be submitted as PRs to the [ArduPilot/Pymavlink](https://github.com/ArduPilot/pymavlink) repository.

The sections below explain how to contribute to each category and how to raise a pull request.

## How to Contribute Complex Changes

* Open a pull request against the RFC repository containing a new RFC number <https://github.com/mavlink/rfcs> and use the template in the 0000 RFC.
* Reach out to the community on Slack and the [mailing list](https://groups.google.com/forum/#!forum/mavlink) to raise awareness
* 通过进一步支持拉动请求来解决关注问题

## How to Contribute Simple Changes

* Open a pull request against the specification repository: <https://github.com/mavlink/mavlink>
* Reach out to the community on Slack and the [mailing list](https://groups.google.com/forum/#!forum/mavlink) to raise awareness
* Address concerns by pushing more commits to the pull request

## 如何打开拉请求

1. 第一个[fork and clone](https://help.github.com/articles/fork-a-repo) 项目项目。
2. 在主服务器上创建要素分支
    
        git 结帐 -b mydescriptivrancanchname
        
    
    > **Note***Always* 分支从主分支的新功能。

3. 用描述性承诺消息提交您的更改。

* Include context information, what was fixed, and an [issue number](https://github.com/mavlink/mavlink) \(Github will link these then conveniently\)
* **Example:**
    
    ``` Change the attitude output spec documentation
    
    * Fixes a typo
    * Clarifies that units are radians
        
        Fixes issue #123 ```

4. 测试您的更改 \ (我们可能会要求您在您的 pr 中提供测试结果 \)。

5. 将更改推送到您的存储库:
    
        git 推送来源 mydescriptisbranchname
        

6. 发送 [pull request ](https://github.com/mavlink/mavlink/compare/) 以合并分支中的更改。

## Dev呼叫 {#dev_call}

We have a regular [dev call](../about/support.md#dev_call) that is open to anyone who is interested in contributing to the project!