# 为 mavlink 做贡献

我们遵循[Github 流](https://guides.github.com/introduction/flow/) 开发模式。 贡献分为两个主要方面: 设计和微服务变化包括状态机附带的新特征和新类型接口的消息规范 \ (示例: 参数或任务协议 \)。 这些都是需要大量审查的重大贡献, 应该有 rfc 的拉动请求, <https://github.com/mavlink/rfcs>。 协议规范和文档更改通常是影响较小的更改, 可以作为针对此存储库的拉请求直接引发。

下面我们将解释为每个类别做出贡献的过程, 以及如何提出拉请求。

## 如何贡献设计和微服务的变化

* 对包含新 rfc 号的 rfc 存储库打开一个拉请求 <https://github.com/mavlink/rfcs> 并使用 0000 rfc 中的模板。
* 与Slack社区联系，在<http://discuss.dronecode.org>上提高认识
* 通过进一步支持拉动请求来解决关注问题

## 如何促成协议规范的更改

* 针对规格存储库打开拉动请求：<https://github.com/mavlink/mavlink>
* 与Slack社区联系，在<http://discuss.dronecode.org>上提高认识
* 通过进一步支持拉动请求来解决关注问题

## 如何打开拉请求

1. 第一个[fork and clone](https://help.github.com/articles/fork-a-repo) 项目项目。
2. 在主服务器上创建要素分支
    
        git 结帐 -b mydescriptivrancanchname
        
    
    > **Note***Always* 分支从主分支的新功能。

3. 用描述性承诺消息提交您的更改。

* 包含背景信息，固定内容，以及 [发布号](https://github.com/mavlink/mavlink)\(Github 将连接这些，然后是方便的\)
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