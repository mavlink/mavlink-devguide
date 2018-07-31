# Contributing to MAVLink

We follow the [Github flow](https://guides.github.com/introduction/flow/) development model. Contributions fall into two main categories: Design and micro-service changes include new features that come with a state machine and message specifications for a new type of interface \(examples: parameter or mission protocol\). These are major contributions requiring a lot of vetting and should come with a RFC pull request in [https://github.com/mavlink/rfcs](https://github.com/mavlink/rfcs). Protocol specification and documentation changes are usually changes with less impact and can be directly raised as pull requests against this repository.

Below we explain the processes for contributing to each category and how to raise a pull request.

## How to Contribute Design and Micro-service Changes

* Open a pull request against the RFC repository containing a new RFC number [https://github.com/mavlink/rfcs](https://github.com/mavlink/rfcs) and use the template in the 0000 RFC.
* Reach out to the community on Slack and on [http://discuss.dronecode.org](http://discuss.dronecode.org) to raise awareness
* Address concerns by pushing more commits to the pull request

## How to Contribute Protocol Specification Changes

* Open a pull request against the specification repository: [https://github.com/mavlink/mavlink](https://github.com/mavlink/mavlink)
* Reach out to the community on Slack and on [http://discuss.dronecode.org](http://discuss.dronecode.org) to raise awareness
* Address concerns by pushing more commits to the pull request

## How to Open a Pull Request

1. First [fork and clone](https://help.github.com/articles/fork-a-repo) the project project.
2. Create a feature branch off master

   ```
   git checkout -b mydescriptivebranchname
   ```

   > **Note** _Always_ branch off master for new features.

3. Commit your changes with a descriptive commit message.

   * Include context information, what was fixed, and an [issue number](https://github.com/mavlink/mavlink) \(Github will link these then conveniently\)
   * **Example:**

     ```
     Change the attitude output spec documentation

     - Fixes a typo
     - Clarifies that units are radians

     Fixes issue #123
     ```

4. Test your changes \(we may ask you for test results in your PR\).

5. Push changes to your repo:

   ```
   git push origin mydescriptivebranchname
   ```

6. Send a [pull request](https://github.com/mavlink/mavlink/compare/) to merge changes in the branch.

## Support {#support}

General support channels are covered in [Forums & Chat](../README.md#support).

### Weekly Dev Call {#dev_call}

MAVLink developers, adopting companies and the surrounding community of users meet weekly to help define the direction of the project, discuss RFCs, Issues and have a Q&A session.

#### Who should attend: {#who-should-attend}

* Core project maintainers
* Component maintainers
* Dronecode members
* Community members
* Anyone interested in the development of MAVLink

> The dev call is open to all interested developers \(not just the dev team\). This is a great opportunity to meet the team and contribute to the ongoing development of the project.

#### Schedule {#schedule}

There are two bi-weekly calls on the same day: One for a Asia-Europe overlap and one for a Europe-Americas overlap.

> **Tip** Both calls are shown as *MAVLink Co-ordination* in the [Dronecode calendar](https://www.dronecode.org/calendar/).

* **Asia-Europe**: [https://zoom.us/j/832229956](https://zoom.us/j/832229956)
  * **TIME**: Wednesday 9:00AM CET, 3:00 PM China, 5:00PM ACT
  * Zoom Meeting ID: 832 229 956
* **Europe-Americas**: [https://zoom.us/j/170266847](https://zoom.us/j/170266847)
  * **TIME**: Wednesday 6:00PM CET, 12:00AM EST, 9:00AM PST
  * Zoom Meeting ID: 170 266 847
* **Dial\(for higher quality, dial a number based on your current location\)**:

  * **Switzerland**: +41 \(0\) 31 528 0988
  * **US**: +1 646 876 9923 or +1 669 900 6833 or +1 408 740 3766
  * **Germany**: +49 \(0\) 30 3080 6188
  * **Mexico**: +52 554 161 4288
  * **Australia**: +61 \(0\) 2 8015 2088
  * **United Kingdom**: +44 \(0\) 20 3695 0088
  * **South Korea**: +82 \(0\) 2 6022 2322
  * **Spain**: +34 91 198 0188
  * [**International numbers available**](https://zoom.us/u/Q40ZTqiJ)

* **Nominate Issues and PRs** for the call with the [**Dev Call**](https://github.com/mavlink/mavlink/labels/Dev%20Call) label on Github.



