# 为 mavlink 做贡献

我们遵循[Github 流](https://guides.github.com/introduction/flow/) 开发模式。 贡献分为两个主要方面: 设计和微服务变化包括状态机附带的新特征和新类型接口的消息规范 \ (示例: 参数或任务协议 \)。 这些都是需要大量审查的重大贡献, 应该有 rfc 的拉动请求, <https://github.com/mavlink/rfcs>。 协议规范和文档更改通常是影响较小的更改, 可以作为针对此存储库的拉请求直接引发。

Below we explain the processes for contributing to each category and how to raise a pull request.

## How to Contribute Design and Micro-service Changes

* Open a pull request against the RFC repository containing a new RFC number <https://github.com/mavlink/rfcs> and use the template in the 0000 RFC.
* Reach out to the community on Slack and on <http://discuss.dronecode.org> to raise awareness
* Address concerns by pushing more commits to the pull request

## How to Contribute Protocol Specification Changes

* Open a pull request against the specification repository: <https://github.com/mavlink/mavlink>
* Reach out to the community on Slack and on <http://discuss.dronecode.org> to raise awareness
* Address concerns by pushing more commits to the pull request

## How to Open a Pull Request

1. First [fork and clone](https://help.github.com/articles/fork-a-repo) the project project.
2. Create a feature branch off master
    
        git checkout -b mydescriptivebranchname
        
    
    > **Note** *Always* branch off master for new features.

3. Commit your changes with a descriptive commit message.

* Include context information, what was fixed, and an [issue number](https://github.com/mavlink/mavlink) \(Github will link these then conveniently\)
* **Example:**
    
    ``` Change the attitude output spec documentation
    
    * Fixes a typo
    * Clarifies that units are radians
        
        Fixes issue #123 ```

4. Test your changes \(we may ask you for test results in your PR\).

5. Push changes to your repo:
    
        git push origin mydescriptivebranchname
        

6. Send a [pull request](https://github.com/mavlink/mavlink/compare/) to merge changes in the branch.

## Dev Call {#dev_call}

We have a regular [dev call](../about/support.md#dev_call) that is open to anyone who is interested in contributing to the project!