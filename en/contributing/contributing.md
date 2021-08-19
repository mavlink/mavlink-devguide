# Contributing to MAVLink

We follow the [Github flow](https://guides.github.com/introduction/flow/) development model.

Contributions are divided into several categories: 
- Complicated changes that require significant review should be initiated using an RFC pull request in [mavlink/rfcs](https://github.com/mavlink/rfcs).
  This is primarily intended for new microservice interface definitions, as these require discussion of both messages and message sequences (state machines) \(examples: parameter or mission protocol\). Depending on the scope of the change, it may also be required when *modifying* a microservice.
- Less complex changes should be submitted as a PRs to the [mavlink/mavlink](https://github.com/mavlink/mavlink) repository. This includes message additions/changes that do not affect a state machine.
- Changes to mavgen generator code should be submitted as PRs to the [ArduPilot/Pymavlink](https://github.com/ArduPilot/pymavlink) repository.

The sections below explain how to contribute to each category and how to raise a pull request.

## How to Contribute Simple Changes

* Open a pull request against the specification repository: [https://github.com/mavlink/mavlink](https://github.com/mavlink/mavlink)
* Reach out to the community on Slack and the [mailing list](https://groups.google.com/forum/#!forum/mavlink) to raise awareness
* Address concerns by pushing more commits to the pull request

## How to Contribute Complex Changes

* Open a pull request against the RFC repository containing a new RFC number [https://github.com/mavlink/rfcs](https://github.com/mavlink/rfcs) and use the template in the 0000 RFC.
* Reach out to the community on Slack and the [mailing list](https://groups.google.com/forum/#!forum/mavlink) to raise awareness
* Address concerns by pushing more commits to the pull request

## How to Contribute to Mavgen

Changes to the [mavgen](../getting_started/generate_libraries.md#mavgen) generator must be added as pull requests through the [ArduPilot/pymavlink](https://github.com/ArduPilot/pymavlink) project.

Changes to existing generator code (e.g. bug fixes) are automatically tested by continuous integration (github actions).
Once you have made against your PR pass, the changes will be reviewed by a project team member.

More significant changes to the generator, such as the addition of a new programming language, will require:
- Project team should be able to commit to supporting the generator.
- `common.xml` and all official dialect XML files should parse, validate, and be able to encode/decode for all the messages.
- Failures should be handled gracefully (not result in exceptions/segfaults).
- Enum values that are not explicitly defined in XML should be automatically and sequentially allocated.
- Test code to validate the above.

Ideally:
- Libraries should support both MAVLink 2 and MAVLink 1
- Any message with arbitrary field values can be successfully encoded and decoded.
- Errors/warnings should be reported for invalid payloads - e.g. oversize, duplicate command or message ids, etc.
- Deep dialect inclusion/nesting should be supported (minimum is 5 levels).

## How to Contribute Stand Alone Generators

We would prefer that new languages are supported via [mavgen](../getting_started/generate_libraries.md#mavgen) rather than "standalone generators", as this provides a consistent inteface for end users, and ensures that source files are parsed and handled consistently.

That said will consider moving stand-alone generators into the MAVLink project under the same conditions as for new mavgen generator code (see section above).
Primarily this means that the team developing the generator must provide sufficient validation that the generator works and commitment to support it.


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


## Dev Call {#dev_call}

We have a regular [dev call](../about/support.md#dev_call) that is open to anyone who is interested in contributing to the project!
