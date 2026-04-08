<p align="center">
  <a href="https://www.cobo.com/developers">
    <img src="v1/images/instroduction.png"/>
  </a>
</p>

<div align="center">
  <h1>Cobo Developer Hub</h1>
  <br />
  <br />
  <a href="https://www.cobo.com/developers/v2/api-references/overview/changelog">Developer Hub</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://www.cobo.com/news">News</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://discord.gg/FaZwQ9WYpj">Discord</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://twitter.com/Cobo_Global">Twitter</a>
  <br />
</div>

<br />

## About Cobo
Cobo is a trusted leader in digital asset custody and wallet infrastructure solutions. Founded in 2017 by blockchain pioneers, Cobo is trusted by more than 500 organizations worldwide, safeguarding billions of dollars in assets with a zero-incident security track record.

Today, Cobo provides the industry’s only unified digital asset wallet platform that integrates all 4 wallet technologies in one place – Custodial Wallets, MPC Wallets, Smart Contract Wallets, and Exchange Wallets. By combining a comprehensive suite of wallet solutions with advanced risk controls and developer tools, Cobo empowers organizations and developers to innovate and scale with ease.

Visit [Cobo](https://www.cobo.com) for more information.

## Get started

The Developer Hub mainly includes the following resources.:

- **[Custodial Wallets](https://manuals.cobo.com/en/portal/custodial-wallets/introduction)**. Cobo Custodial Wallets are a secure and regulated custodial wallet solution, designed specifically for institutions to manage digital assets. Custodial Wallets take the complexity out of securing your assets by managing the private keys on your behalf. 
- **[MPC Wallets](https://manuals.cobo.com/en/portal/mpc-wallets/introduction)**. Cobo MPC Wallets leverages advanced Multi-Party Computation (MPC) technology to implement a Threshold Signature Scheme (TSS). Cobo Portal offers two types of MPC Wallets: Organization-Controlled Wallets and User-Controlled Wallets.
- **[Smart Contract Wallets](https://manuals.cobo.com/en/portal/smart-contract-wallets/introduction)**. Cobo Smart Contract Wallets support a myriad of smart contract wallets, prominently featuring Safe{Wallet} alongside other account abstraction wallets. 
- **[Exchange Wallets](https://manuals.cobo.com/en/portal/exchange-wallets/introduction)**. Cobo Portal’s Exchange Wallets are your one-stop solution for managing multiple exchange accounts effortlessly.

## GitHub repository directory
Currently we offer  The content for WaaS 1.0 and WaaS 2.0 on the Developer Hub at the same time. You could switch between the two version by selecting the **Version 1.0** and the **Version 2.0** buttons. 

Below is the repository directory structure for the two versions:

- `v2`
  - `api-references`: The content under the **API References** tab, which contains the reference information for the WaaS 2.0 API.
  - `cobo_waas2_openapi_spec`:The WaaS 2.0 OpenAPI spec.
  - `guides`: (Coming soon) The content under the **Guides** tab, which contains instructions on implementing basic and advanced features.
  - `developer-tools`: (Coming soon) The content under the **Developer Tools** tab, which contains documentation for the WaaS SDKs.
  - `faqs`: (Coming soon) The content under the **FAQs** tab, which contains answers to frequently asked questions.


- `v1`
  - `overview`: The content under the **Documentation** tab, which contains introduction to the WaaS 1.0 service and wallets.
  - `get-started/overview`: The content under the **Get Started** tab, which explains basic workflows for different types of wallets.
  - `api-references`: The content under the **API References** tab, which contains the reference information for the WaaS 1.0 API.
  - `guides/howtos`: The content under the **Guides** tab, which contains instructions on implementing basic and advanced features.
  - `sdk-and-tools`: The content under the **SDKs and Tools** tab, which contains documentation for the WaaS 1.0 SDKs and useful tools.
  - `faqs`: The content under the **FAQs** tab, which contains answers to frequently asked questions.

## Contributing

PRs are always welcome! To get started, follow this section to build Developer Hub on your local machine.

1. Clone the repository.

  ```shell
  git clone git@github.com:CoboGlobal/developer-site.git
  ```

2. Install Mintlify.

  ```shell
  npm i -g mintlify
  ```

3. Go to the root directory (where you can find the `mint.json` file) and run the following command:

  ```shell
  mintlify dev
  ```

The documentation website is now available at `http://localhost:3000`.

Developer Hub is built on Mintlify that uses a syntax very similar to markdown. For more usage instructions, see [Mintlify Quickstart](https://mintlify.com/docs/quickstart).

When you complete the modifications locally and make sure no error or issue occur when you preview, proceed with the standard [Fork & Pull Request](https://gist.github.com/Chaser324/ce0505fbed06b947d962) process for submission.

If you regenerate WaaS 2.0 API reference MDX from OpenAPI (for example via `build_scripts/build_mdx_and_code.sh`), Mintlify’s generator does not include the Cobo WaaS skill reminder. The pipeline runs [`scripts/ensure_waas_skill_reminder_mdx.py`](scripts/ensure_waas_skill_reminder_mdx.py) afterward; if you generate MDX another way, run `python scripts/ensure_waas_skill_reminder_mdx.py` from the repository root before committing.

## Contact us

[Join the discord 👉](https://discord.gg/FaZwQ9WYpj)
<br />
[Join the telegram 👉](https://t.me/coboglobal)
<br />
[Follow our twitter 👉](https://twitter.com/Cobo_Global)
<br />
[Follow our linkedln 👉](https://www.linkedin.com/company/cobo-global/)

## License

The code in this repository is developed and distributed under the
GPL 3.0 license. See [LICENSE](LICENSE) for details.
