# Account

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/account
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [Most commonly used](index.md) / Account
> Canonical entity: `Account`

Accounts are what businesses use to track transactions. Accounts can track money coming in (income or revenue) and going out (expenses). They can also track the value of things (assets), like vehicles and equipment. There are five basic account types: asset, liability, income, expense, and equity. Accounts are part of the chart of accounts, the unique list of accounts each business puts together to do their accounting. Accountants often call accounts "ledgers". Learn more about accounts and the chart of accounts. The account object is what you'll use to do actions with the end-users accounts. Note: If you need to delete an account, set the `Active` attribute to false in an object update request. This makes it inactive. The account itself isn't permanently deleted, but is hidden for display purposes. References to inactive objects remain intact.

<details>
<summary>Show more information</summary>

For France locales, only:

- If an Account object is created under the category where the `purchSaleLocationRequired` attribute is true in the master category list, the system does not allow more then one account to be created for the same location. For example, if an expense account 606401 is associated with location `Within France` under account category 6064, then the system does not allow another account (6064XX) to be created with the same location `Within France` under the same 6064 account category.
- If Account is created under the category where both `purchSaleLocationRequired` attribute and `vatCodeRequired` attribute is true in the master category list, the system does not allow more then one account to be created for the same location and VAT code combination. For example, if an income account 703001 is associated with location `Within France` and `20 % TVA FR` VAT rate under account category 703, then the system does not allow another account (703XXX) to be created with the same location `Within France` and `20 % TVA FR` VAT rate under same account category 703.
- If Account is not used in any transaction then the system allows edits on fields `AcctNum`, `Name`, `TxnLocationType`, `TaxCodeRef`, and `AccountAlias`.
- If Account is used in a transaction and transaction is soft closed then system will not allow edits for `AcctNum`, `Name`, `TxnLocationType`, and `TaxCodeRef`.
- If account is used in Transaction and transaction is not soft closed then system will not allow edits for `TxnLocationType` and `TaxCodeRef`.
- QuickBooks Online uses a master account list for CRUD operations, which is driven from the French generally accepted Plan Comptable General (PCG) list. This list contains an array of JSON objects, with each entry corresponding to a number prefix in the PCG list.

Master category list object format -

#### ATTRIBUTES

| Name | Description |
| --- | --- |
| detailType | DetailType of the account in QuickBooks Online. |
| name | Default name of the account. |
| accountAlias | Default accountAlias for account. |
| number | Account starting with this number falls under this category. |
| nonPosting | If true, account creation for this category is not allowed. |
| purchSaleLocationRequired | If true, the system allows account created under this category to be associated with TxnLocationType. |
| defaultPurchSaleLocation | Default location for account created. |
| defaultTaxCode | Default TaxCode associated with the account. |
| canSetOpeningBalance | If true, opening balance can be set for these accounts. |
| vatCodeRequired | If true, the system allows a VAT code to be associated with this account. |
| journalCodeRequired | If true, the system allows a JournalCode object to be associated with this account. |
| itemCategoryType | Accounts created under this category can be associated with particular type of item. For example, if Array contains PRODUCT then the account created can be associated with item of type PRODUCT only. |
| includedTxnApplicableSet | includedTxnApplicableSet |
| excludedTxnApplicableSet | includedTxnApplicableSet |
| bankAccountFilterTypes | includedTxnApplicableSet |

</details>

## Sample account object

### accountresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `Name`

Required: Required
Type: `String`
Traits: filterable, sortable
Max length: max 100 characters

User recognizable name for the Account. `Account.Name` attribute must not contain double quotes (") or colon (:).

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `AcctNum`

Required: Conditionally required
Type: `String`

User-defined account number to help the user in identifying the account within the chart-of-accounts and in deciding what should be posted to the account. The `Account.AcctNum` attribute must not contain colon (:).

- Name must be unique.

For French Locales:

Max length for `Account.AcctNum`:

- AU & CA: 20 characters.
- US, UK & IN: 7 characters

#### `SubAccount`

Type: `Boolean`
Traits: read only, system defined, filterable, sortable

Specifies whether this object represents a parent (false) or subaccount (true). Please note that accounts of these types - `OpeningBalanceEquity`, `UndepositedFunds`, `RetainedEarnings`, `CashReceiptIncome`, `CashExpenditureExpense`, `ExchangeGainOrLoss` cannot have a sub account and cannot be a sub account of another account.

#### `Classification`

Type: `String`
Traits: read only, system defined, filterable
Default: derived from AccountType and AccountSubtype

The classification of an account. Not supported for non-posting accounts. Valid values include: `Asset`, `Equity`, `Expense`, `Liability`, `Revenue`

#### `FullyQualifiedName`

Type: `String`
Traits: read only, system defined, filterable, sortable

Fully qualified name of the object; derived from `Name` and `ParentRef`. The fully qualified name prepends the topmost parent, followed by each subaccount separated by colons and takes the form of `Parent:Account1:SubAccount1:SubAccount2`. System generated. Limited to 5 levels.

#### `TxnLocationType`

Type: `String`
Default: WithinFrance
Minor version: 5
Locales: FR

The account location. Valid values include:

`WithinFrance`

`FranceOverseas`

`OutsideFranceWithEU`

`OutsideEU`

For France locales, only.

#### `AccountType`

Type: `AccountTypeEnum`
Traits: filterable

A detailed account classification that specifies the use of this account. The type is based on the Classification.

<details>
<summary>Show child attributes</summary>

#### ASSET

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Bank | **Default**<br> CashOnHand (default)<br> Checking <br> MoneyMarket<br> RentsHeldInTrust<br> Savings<br> TrustAccounts<br> **Available with minor version: 13**<br> CashAndCashEquivalents<br> OtherEarMarkedBankAccounts<br> |
| Other Current Asset | **Default**<br> AllowanceForBadDebts<br> DevelopmentCosts<br> EmployeeCashAdvances (default)<br> OtherCurrentAssets<br> Inventory<br> Investment_MortgageRealEstateLoans<br> Investment_Other<br> Investment_TaxExemptSecurities<br> Investment_USGovernmentObligations<br> LoansToOfficers<br> LoansToOthers<br> LoansToStockholders<br> PrepaidExpenses<br> Retainage<br> UndepositedFunds<br> **Available with minor version: 13**<br> AssetsAvailableForSale<br> BalWithGovtAuthorities<br> CalledUpShareCapitalNotPaid<br> ExpenditureAuthorisationsAndLettersOfCredit<br> GlobalTaxDeferred<br> GlobalTaxRefund<br> InternalTransfers<br> OtherConsumables<br> ProvisionsCurrentAssets<br> ShortTermInvestmentsInRelatedParties<br> ShortTermLoansAndAdvancesToRelatedParties<br> TradeAndOtherReceivables<br> |
| Fixed Asset | **Default**<br> AccumulatedDepletion<br> AccumulatedDepreciation<br> DepletableAssets<br> FixedAssetComputers<br> FixedAssetCopiers<br> FixedAssetFurniture<br> FixedAssetPhone<br> FixedAssetPhotoVideo<br> FixedAssetSoftware<br> FixedAssetOtherToolsEquipment<br> FurnitureAndFixtures (default)<br> Land<br> LeaseholdImprovements<br> OtherFixedAssets<br> AccumulatedAmortization<br> Buildings<br> IntangibleAssets<br> MachineryAndEquipment<br> Vehicles<br> **Available with minor version: 13**<br> AssetsInCourseOfConstruction<br> CapitalWip<br> CumulativeDepreciationOnIntangibleAssets<br> IntangibleAssetsUnderDevelopment<br> LandAsset<br> NonCurrentAssets<br> ParticipatingInterests<br> ProvisionsFixedAssets<br> |
| Other Asset | **Default**<br> LeaseBuyout<br> OtherLongTermAssets<br> SecurityDeposits<br> AccumulatedAmortizationOfOtherAssets<br> Goodwill<br> Licenses (default)<br> OrganizationalCosts<br> **Available with minor version: 13**<br> AssetsHeldForSale<br> AvailableForSaleFinancialAssets<br> DeferredTax<br> Investments<br> LongTermInvestments<br> LongTermLoansAndAdvancesToRelatedParties<br> OtherIntangibleAssets<br> OtherLongTermInvestments<br> OtherLongTermLoansAndAdvances<br> PrepaymentsAndAccruedIncome<br> ProvisionsNonCurrentAssets<br> |
| Accounts Receivable | **Default**<br> Accounts Receivable<br> |

#### EQUITY

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Equity | **Default** <br> OpeningBalanceEquity (default)<br> PartnersEquity<br> RetainedEarnings<br> AccumulatedAdjustment<br> OwnersEquity<br> PaidInCapitalOrSurplus<br> ​PartnerContributions<br> PartnerDistributions<br> PreferredStock<br> CommonStock<br> TreasuryStock<br> EstimatedTaxes<br> Healthcare<br> PersonalIncome<br> PersonalExpense<br> **Available with minor version: 13**<br> AccumulatedOtherComprehensiveIncome<br> CalledUpShareCapital<br> CapitalReserves<br> DividendDisbursed<br> EquityInEarningsOfSubsiduaries<br> InvestmentGrants<br> MoneyReceivedAgainstShareWarrants<br> OtherFreeReserves<br> ShareApplicationMoneyPendingAllotment<br> ShareCapital<br> Funds<br> |

#### EXPENSE

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Expense | **Default** <br> AdvertisingPromotional<br> BadDebts<br> BankCharges<br> CharitableContributions<br> CommissionsAndFees<br> Entertainment<br> EntertainmentMeals<br> EquipmentRental<br> FinanceCosts<br> GlobalTaxExpense<br> Insurance<br> InterestPaid<br> LegalProfessionalFees<br> OfficeExpenses<br> OfficeGeneralAdministrativeExpenses<br> OtherBusinessExpenses<br> OtherMiscellaneousServiceCost<br> PromotionalMeals<br> RentOrLeaseOfBuildings<br> RepairMaintenance<br> ShippingFreightDelivery<br> SuppliesMaterials<br> Travel (default)<br> TravelMeals<br> Utilities<br> Auto<br> CostOfLabor<br> DuesSubscriptions<br> PayrollExpenses<br> TaxesPaid<br> UnappliedCashBillPaymentExpense<br> Utilities<br> **Available with minor version: 13**<br> AmortizationExpense<br> AppropriationsToDepreciation<br> BorrowingCost<br> CommissionsAndFees<br> DistributionCosts<br> ExternalServices<br> ExtraordinaryCharges<br> IncomeTaxExpense<br> LossOnDiscontinuedOperationsNetOfTax<br> ManagementCompensation<br> OtherCurrentOperatingCharges<br> OtherExternalServices<br> OtherRentalCosts<br> OtherSellingExpenses<br> ProjectStudiesSurveysAssessments<br> PurchasesRebates<br> ShippingAndDeliveryExpense<br> StaffCosts<br> Sundry<br> TravelExpensesGeneralAndAdminExpenses<br> TravelExpensesSellingExpense<br> |
| Other Expense | **Default**<br> Depreciation (default)<br> ExchangeGainOrLoss<br> OtherMiscellaneousExpense<br> PenaltiesSettlements<br> Amortization<br> GasAndFuel<br> HomeOffice<br> HomeOwnerRentalInsurance<br> OtherHomeOfficeExpenses<br> MortgageInterest<br> RentAndLease<br> RepairsAndMaintenance<br> ParkingAndTolls<br> Vehicle<br> VehicleInsurance<br> VehicleLease<br> VehicleLoanInterest<br> VehicleLoan<br> VehicleRegistration<br> VehicleRepairs<br> OtherVehicleExpenses<br> Utilities<br> WashAndRoadServices <br> **Available with minor version: 13**<br> DeferredTaxExpense<br> Depletion<br> ExceptionalItems<br> ExtraordinaryItems<br> IncomeTaxOtherExpense<br> MatCredit<br> PriorPeriodItems<br> TaxRoundoffGainOrLoss<br> |
| Cost of Goods Sold | **Default**<br> EquipmentRentalCos<br> OtherCostsOfServiceCos<br> ShippingFreightDeliveryCos<br> SuppliesMaterialsCogs<br> CostOfLaborCos (default)<br> **Available with minor version: 13**<br> CostOfSales<br> FreightAndDeliveryCost<br> |

#### LIABILITY

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Accounts Payable | **Default** <br> Accounts Payable<br> **Available with minor version: 13**<br> OutstandingDuesMicroSmallEnterprise<br> OutstandingDuesOtherThanMicroSmallEnterprise<br> |
| Credit Card | **Default**<br> Credit Card <br> |
| Long Term Liability | **Default**<br> NotesPayable (default)<br> OtherLongTermLiabilities<br> ShareholderNotesPayable<br> **Available with minor version: 13**<br> AccrualsAndDeferredIncome<br> AccruedLongLermLiabilities<br> AccruedVacationPayable<br> BankLoans<br> DebtsRelatedToParticipatingInterests<br> DeferredTaxLiabilities<br> GovernmentAndOtherPublicAuthorities<br> GroupAndAssociates<br> LiabilitiesRelatedToAssetsHeldForSale<br> LongTermBorrowings<br> LongTermDebit<br> LongTermEmployeeBenefitObligations<br> ObligationsUnderFinanceLeases<br> OtherLongTermProvisions<br> ProvisionForLiabilities<br> ProvisionsNonCurrentLiabilities<br> StaffAndRelatedLongTermLiabilityAccounts<br> |
| Other Current Liability | **Default**<br> DirectDepositPayable<br> LineOfCredit<br> LoanPayable<br> GlobalTaxPayable<br> GlobalTaxSuspense<br> OtherCurrentLiabilities (default)<br> PayrollClearing<br> PayrollTaxPayable<br> PrepaidExpensesPayable<br> RentsInTrustLiability<br> TrustAccountsLiabilities<br> FederalIncomeTaxPayable<br> InsurancePayable<br> SalesTaxPayable<br> StateLocalIncomeTaxPayable <br> **Available with minor version: 13**<br> AccruedLiabilities<br> CurrentLiabilities<br> CurrentPortionEmployeeBenefitsObligations<br> CurrentPortionOfObligationsUnderFinanceLeases<br> CurrentTaxLiability<br> DividendsPayable<br> DutiesAndTaxes<br> InterestPayables<br> ProvisionForWarrantyObligations<br> ProvisionsCurrentLiabilities<br> ShortTermBorrowings<br> SocialSecurityAgencies<br> StaffAndRelatedLiabilityAccounts<br> SundryDebtorsAndCreditors<br> TradeAndOtherPayables<br> |

#### REVENUE

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Income | **Default** <br> NonProfitIncome<br> OtherPrimaryIncome (default)<br> SalesOfProductIncome<br> ServiceFeeIncome<br> DiscountsRefundsGiven<br> UnappliedCashPaymentIncome<br> **Available with minor version: 13**<br> CashReceiptIncome<br> OperatingGrants<br> OtherCurrentOperatingIncome<br> OwnWorkCapitalized<br> RevenueGeneral<br> SalesRetail<br> SalesWholesale<br> SavingsByTaxScheme<br> |
| Other Income | **Default**<br> DividendIncome<br> InterestEarned<br> OtherInvestmentIncome (default)<br> OtherMiscellaneousIncome<br> TaxExemptInterest <br> **Available with minor version: 13**<br> GainLossOnSaleOfFixedAssets<br> GainLossOnSaleOfInvestments<br> LossOnDisposalOfAssets<br> OtherOperatingIncome<br> UnrealisedLossOnSecuritiesNetOfTax<br> |

</details>

#### `CurrentBalanceWithSubAccounts`

Type: `Decimal`
Traits: read only, filterable, sortable

Specifies the cumulative balance amount for the current Account and all its sub-accounts.

#### `AccountAlias`

Type: `String`
Default: Account.Name
Minor version: 5
Locales: FR

A user friendly name for the account. It must be unique across all account categories. For France locales, only. For example, if an account is created under category 211 with `AccountAlias` of `Terrains`, then the system does not allow creation of an account with same `AccountAlias` of `Terrains` for any other category except 211. In other words, 211001 and 215001 accounts cannot have same AccountAlias because both belong to different account category. For France locales, only.

#### `TaxCodeRef`

Type: `ReferenceType`
Minor version: 3
Locales: GB, AU, IN, CA, FR

Reference to the default tax code used by this account. Tax codes are referenced by the `TaxCode.Id` in the TaxCode object. Available when endpoint is invoked with the `minorversion=3` query parameter. For global locales, only.

<details>
<summary>Child attributes for `TaxCodeRef`</summary>

##### referencetype

Model type: `object`

###### `value`

Required: Required
Type: `string`

The ID for the referenced object as found in the Id field of the object payload. The context is set by the type of reference and is specific to the QuickBooks company file.

###### `name`

Required: Optional
Type: `string`

An identifying name for the object being referenced by `value` and is derived from the field that holds the common name of that object. This varies by context and specific type of object referenced. For example, references to a Customer object use `Customer.DisplayName` to populate this field. Optionally returned in responses, implementation dependent.

</details>

#### `AccountSubType`

Type: `String`
Traits: filterable

The account sub-type classification and is based on the AccountType value.

<details>
<summary>Show child attributes</summary>

#### ASSET

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Bank | **Default**<br> CashOnHand (default)<br> Checking <br> MoneyMarket<br> RentsHeldInTrust<br> Savings<br> TrustAccounts<br> **Available with minor version: 13**<br> CashAndCashEquivalents<br> OtherEarMarkedBankAccounts<br> |
| Other Current Asset | **Default**<br> AllowanceForBadDebts<br> DevelopmentCosts<br> EmployeeCashAdvances (default)<br> OtherCurrentAssets<br> Inventory<br> Investment_MortgageRealEstateLoans<br> Investment_Other<br> Investment_TaxExemptSecurities<br> Investment_USGovernmentObligations<br> LoansToOfficers<br> LoansToOthers<br> LoansToStockholders<br> PrepaidExpenses<br> Retainage<br> UndepositedFunds<br> **Available with minor version: 13**<br> AssetsAvailableForSale<br> BalWithGovtAuthorities<br> CalledUpShareCapitalNotPaid<br> ExpenditureAuthorisationsAndLettersOfCredit<br> GlobalTaxDeferred<br> GlobalTaxRefund<br> InternalTransfers<br> OtherConsumables<br> ProvisionsCurrentAssets<br> ShortTermInvestmentsInRelatedParties<br> ShortTermLoansAndAdvancesToRelatedParties<br> TradeAndOtherReceivables<br> |
| Fixed Asset | **Default**<br> AccumulatedDepletion<br> AccumulatedDepreciation<br> DepletableAssets<br> FixedAssetComputers<br> FixedAssetCopiers<br> FixedAssetFurniture<br> FixedAssetPhone<br> FixedAssetPhotoVideo<br> FixedAssetSoftware<br> FixedAssetOtherToolsEquipment<br> FurnitureAndFixtures (default)<br> Land<br> LeaseholdImprovements<br> OtherFixedAssets<br> AccumulatedAmortization<br> Buildings<br> IntangibleAssets<br> MachineryAndEquipment<br> Vehicles<br> **Available with minor version: 13**<br> AssetsInCourseOfConstruction<br> CapitalWip<br> CumulativeDepreciationOnIntangibleAssets<br> IntangibleAssetsUnderDevelopment<br> LandAsset<br> NonCurrentAssets<br> ParticipatingInterests<br> ProvisionsFixedAssets<br> |
| Other Asset | **Default**<br> LeaseBuyout<br> OtherLongTermAssets<br> SecurityDeposits<br> AccumulatedAmortizationOfOtherAssets<br> Goodwill<br> Licenses (default)<br> OrganizationalCosts<br> **Available with minor version: 13**<br> AssetsHeldForSale<br> AvailableForSaleFinancialAssets<br> DeferredTax<br> Investments<br> LongTermInvestments<br> LongTermLoansAndAdvancesToRelatedParties<br> OtherIntangibleAssets<br> OtherLongTermInvestments<br> OtherLongTermLoansAndAdvances<br> PrepaymentsAndAccruedIncome<br> ProvisionsNonCurrentAssets<br> |
| Accounts Receivable | **Default**<br> Accounts Receivable<br> |

#### EQUITY

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Equity | **Default** <br> OpeningBalanceEquity (default)<br> PartnersEquity<br> RetainedEarnings<br> AccumulatedAdjustment<br> OwnersEquity<br> PaidInCapitalOrSurplus<br> ​PartnerContributions<br> PartnerDistributions<br> PreferredStock<br> CommonStock<br> TreasuryStock<br> EstimatedTaxes<br> Healthcare<br> PersonalIncome<br> PersonalExpense<br> **Available with minor version: 13**<br> AccumulatedOtherComprehensiveIncome<br> CalledUpShareCapital<br> CapitalReserves<br> DividendDisbursed<br> EquityInEarningsOfSubsiduaries<br> InvestmentGrants<br> MoneyReceivedAgainstShareWarrants<br> OtherFreeReserves<br> ShareApplicationMoneyPendingAllotment<br> ShareCapital<br> Funds<br> |

#### EXPENSE

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Expense | **Default** <br> AdvertisingPromotional<br> BadDebts<br> BankCharges<br> CharitableContributions<br> CommissionsAndFees<br> Entertainment<br> EntertainmentMeals<br> EquipmentRental<br> FinanceCosts<br> GlobalTaxExpense<br> Insurance<br> InterestPaid<br> LegalProfessionalFees<br> OfficeExpenses<br> OfficeGeneralAdministrativeExpenses<br> OtherBusinessExpenses<br> OtherMiscellaneousServiceCost<br> PromotionalMeals<br> RentOrLeaseOfBuildings<br> RepairMaintenance<br> ShippingFreightDelivery<br> SuppliesMaterials<br> Travel (default)<br> TravelMeals<br> Utilities<br> Auto<br> CostOfLabor<br> DuesSubscriptions<br> PayrollExpenses<br> TaxesPaid<br> UnappliedCashBillPaymentExpense<br> Utilities<br> **Available with minor version: 13**<br> AmortizationExpense<br> AppropriationsToDepreciation<br> BorrowingCost<br> CommissionsAndFees<br> DistributionCosts<br> ExternalServices<br> ExtraordinaryCharges<br> IncomeTaxExpense<br> LossOnDiscontinuedOperationsNetOfTax<br> ManagementCompensation<br> OtherCurrentOperatingCharges<br> OtherExternalServices<br> OtherRentalCosts<br> OtherSellingExpenses<br> ProjectStudiesSurveysAssessments<br> PurchasesRebates<br> ShippingAndDeliveryExpense<br> StaffCosts<br> Sundry<br> TravelExpensesGeneralAndAdminExpenses<br> TravelExpensesSellingExpense<br> |
| Other Expense | **Default**<br> Depreciation (default)<br> ExchangeGainOrLoss<br> OtherMiscellaneousExpense<br> PenaltiesSettlements<br> Amortization<br> GasAndFuel<br> HomeOffice<br> HomeOwnerRentalInsurance<br> OtherHomeOfficeExpenses<br> MortgageInterest<br> RentAndLease<br> RepairsAndMaintenance<br> ParkingAndTolls<br> Vehicle<br> VehicleInsurance<br> VehicleLease<br> VehicleLoanInterest<br> VehicleLoan<br> VehicleRegistration<br> VehicleRepairs<br> OtherVehicleExpenses<br> Utilities<br> WashAndRoadServices <br> **Available with minor version: 13**<br> DeferredTaxExpense<br> Depletion<br> ExceptionalItems<br> ExtraordinaryItems<br> IncomeTaxOtherExpense<br> MatCredit<br> PriorPeriodItems<br> TaxRoundoffGainOrLoss<br> |
| Cost of Goods Sold | **Default**<br> EquipmentRentalCos<br> OtherCostsOfServiceCos<br> ShippingFreightDeliveryCos<br> SuppliesMaterialsCogs<br> CostOfLaborCos (default)<br> **Available with minor version: 13**<br> CostOfSales<br> FreightAndDeliveryCost<br> |

#### LIABILITY

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Accounts Payable | **Default** <br> Accounts Payable<br> **Available with minor version: 13**<br> OutstandingDuesMicroSmallEnterprise<br> OutstandingDuesOtherThanMicroSmallEnterprise<br> |
| Credit Card | **Default**<br> Credit Card <br> |
| Long Term Liability | **Default**<br> NotesPayable (default)<br> OtherLongTermLiabilities<br> ShareholderNotesPayable<br> **Available with minor version: 13**<br> AccrualsAndDeferredIncome<br> AccruedLongLermLiabilities<br> AccruedVacationPayable<br> BankLoans<br> DebtsRelatedToParticipatingInterests<br> DeferredTaxLiabilities<br> GovernmentAndOtherPublicAuthorities<br> GroupAndAssociates<br> LiabilitiesRelatedToAssetsHeldForSale<br> LongTermBorrowings<br> LongTermDebit<br> LongTermEmployeeBenefitObligations<br> ObligationsUnderFinanceLeases<br> OtherLongTermProvisions<br> ProvisionForLiabilities<br> ProvisionsNonCurrentLiabilities<br> StaffAndRelatedLongTermLiabilityAccounts<br> |
| Other Current Liability | **Default**<br> DirectDepositPayable<br> LineOfCredit<br> LoanPayable<br> GlobalTaxPayable<br> GlobalTaxSuspense<br> OtherCurrentLiabilities (default)<br> PayrollClearing<br> PayrollTaxPayable<br> PrepaidExpensesPayable<br> RentsInTrustLiability<br> TrustAccountsLiabilities<br> FederalIncomeTaxPayable<br> InsurancePayable<br> SalesTaxPayable<br> StateLocalIncomeTaxPayable <br> **Available with minor version: 13**<br> AccruedLiabilities<br> CurrentLiabilities<br> CurrentPortionEmployeeBenefitsObligations<br> CurrentPortionOfObligationsUnderFinanceLeases<br> CurrentTaxLiability<br> DividendsPayable<br> DutiesAndTaxes<br> InterestPayables<br> ProvisionForWarrantyObligations<br> ProvisionsCurrentLiabilities<br> ShortTermBorrowings<br> SocialSecurityAgencies<br> StaffAndRelatedLiabilityAccounts<br> SundryDebtorsAndCreditors<br> TradeAndOtherPayables<br> |

#### REVENUE

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Income | **Default** <br> NonProfitIncome<br> OtherPrimaryIncome (default)<br> SalesOfProductIncome<br> ServiceFeeIncome<br> DiscountsRefundsGiven<br> UnappliedCashPaymentIncome<br> **Available with minor version: 13**<br> CashReceiptIncome<br> OperatingGrants<br> OtherCurrentOperatingIncome<br> OwnWorkCapitalized<br> RevenueGeneral<br> SalesRetail<br> SalesWholesale<br> SavingsByTaxScheme<br> |
| Other Income | **Default**<br> DividendIncome<br> InterestEarned<br> OtherInvestmentIncome (default)<br> OtherMiscellaneousIncome<br> TaxExemptInterest <br> **Available with minor version: 13**<br> GainLossOnSaleOfFixedAssets<br> GainLossOnSaleOfInvestments<br> LossOnDisposalOfAssets<br> OtherOperatingIncome<br> UnrealisedLossOnSecuritiesNetOfTax<br> |

</details>

#### `CurrentBalance`

Type: `Decimal`
Traits: read only, filterable, sortable

Specifies the balance amount for the current Account. Valid for Balance Sheet accounts.

#### `CurrencyRef`

Required: Optional
Type: `CurrencyRef`
Traits: read only

Reference to the currency in which this account holds amounts.

<details>
<summary>Child attributes for `CurrencyRef`</summary>

##### currencyref

Model type: `object`

###### `value`

Required: Required
Type: `String`

A three letter string representing the ISO 4217 code for the currency. For example, `USD`, `AUD`, `EUR`, and so on.

###### `name`

Required: Optional
Type: `String`

The full name of the currency.

</details>

#### `ParentRef`

Required: Optional
Type: `ReferenceType`
Traits: filterable, sortable

Specifies the Parent AccountId if this represents a SubAccount.

<details>
<summary>Child attributes for `ParentRef`</summary>

##### referencetype

Model type: `object`

###### `value`

Required: Required
Type: `string`

The ID for the referenced object as found in the Id field of the object payload. The context is set by the type of reference and is specific to the QuickBooks company file.

###### `name`

Required: Optional
Type: `string`

An identifying name for the object being referenced by `value` and is derived from the field that holds the common name of that object. This varies by context and specific type of object referenced. For example, references to a Customer object use `Customer.DisplayName` to populate this field. Optionally returned in responses, implementation dependent.

</details>

#### `Description`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: maximum of 100 chars

User entered description for the account, which may include user entered information to guide bookkeepers/accountants in deciding what journal entries to post to the account.

#### `Active`

Required: Optional
Type: `Boolean`
Traits: filterable
Default: true

Whether or not active inactive accounts may be hidden from most display purposes and may not be posted to.

#### `MetaData`

Required: Optional
Type: `ModificationMetaData`

Descriptive information about the object. The MetaData values are set by Data Services and are read only for all applications.

<details>
<summary>Child attributes for `MetaData`</summary>

##### modificationmetadata

Model type: `object`

###### `CreateTime`

Type: `DateTime`
Traits: read only, system defined, filterable, sortable

Time the entity was created in the source domain.

<details>
<summary>Child attributes for `CreateTime`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

###### `LastUpdatedTime`

Type: `DateTime`
Traits: read only, system defined, filterable, sortable

Time the entity was last updated in the source domain.

<details>
<summary>Child attributes for `LastUpdatedTime`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

</details>

#### Example

```json
{
  "Account": {
    "FullyQualifiedName": "MyJobs",
    "domain": "QBO",
    "Name": "MyJobs",
    "Classification": "Asset",
    "AccountSubType": "AccountsReceivable",
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "CurrentBalanceWithSubAccounts": 0,
    "sparse": false,
    "MetaData": {
      "CreateTime": "2014-12-31T09:29:05-08:00",
      "LastUpdatedTime": "2014-12-31T09:29:05-08:00"
    },
    "AccountType": "Accounts Receivable",
    "CurrentBalance": 0,
    "Active": true,
    "SyncToken": "0",
    "Id": "94",
    "SubAccount": false
  },
  "time": "2014-12-31T09:29:05.717-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-13T12:30:07.458-07:00">
  <Account domain="QBO" sparse="false">
    <Id>93</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-07-13T12:34:47-07:00</CreateTime>
      <LastUpdatedTime>2015-07-13T12:34:47-07:00</LastUpdatedTime>
    </MetaData>
    <Name>MyClients</Name>
    <SubAccount>false</SubAccount>
    <FullyQualifiedName>MyClients</FullyQualifiedName>
    <Active>true</Active>
    <Classification>Asset</Classification>
    <AccountType>Accounts Receivable</AccountType>
    <AccountSubType>AccountsReceivable</AccountSubType>
    <CurrentBalance>0</CurrentBalance>
    <CurrentBalanceWithSubAccounts>0</CurrentBalanceWithSubAccounts>
    <CurrencyRef name="United States Dollar">USD</CurrencyRef>
  </Account>
</IntuitResponse>
```

## Create an account

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/account`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

- `Name` must be unique.
- The `Account.Name` attribute must not contain double quotes (") or colon (:).
- The `Account.AcctNum` attribute must not contain a colon (:).

### Request Body

The minimum elements to create an Account object are listed here.

Schema: `accountrequest`

<details>
<summary>Show schema for `accountrequest`</summary>

#### accountrequest

Model type: `object`

##### `Name`

Required: Required
Type: `String`
Traits: filterable, sortable
Max length: max 100 characters

User recognizable name for the Account. `Account.Name` attribute must not contain double quotes (") or colon (:).

##### `AcctNum`

Required: Conditionally required
Type: `String`

User-defined account number to help the user in identifying the account within the chart-of-accounts and in deciding what should be posted to the account. The `Account.AcctNum` attribute must not contain colon (:). For France locales:

Name must be unique.

Length must be between 6 and 20 characters

Must start with the account number from the master category list.

Name limited to alpha-numeric characters.

. Required for France locales

##### `TaxCodeRef`

Required: Conditionally required
Type: `ReferenceType`
Minor version: 3
Locales: GB, AU, IN, CA, FR

Reference to the default tax code used by this account. Tax codes are referenced by the `TaxCode.Id` in the TaxCode object. Available when endpoint is invoked with the `minorversion=3` query parameter. For global locales, only. Required for France locales

<details>
<summary>Child attributes for `TaxCodeRef`</summary>

###### referencetype

Model type: `object`

###### `value`

Required: Required
Type: `string`

The ID for the referenced object as found in the Id field of the object payload. The context is set by the type of reference and is specific to the QuickBooks company file.

###### `name`

Required: Optional
Type: `string`

An identifying name for the object being referenced by `value` and is derived from the field that holds the common name of that object. This varies by context and specific type of object referenced. For example, references to a Customer object use `Customer.DisplayName` to populate this field. Optionally returned in responses, implementation dependent.

</details>

##### `AccountType`

Required: Conditionally required
Type: `AccountTypeEnum`
Traits: filterable

A detailed account classification that specifies the use of this account. The type is based on the Classification.
 Required if AccountSubType is not specified.

<details>
<summary>Show child attributes</summary>

#### ASSET

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Bank | **Default**<br> CashOnHand (default)<br> Checking <br> MoneyMarket<br> RentsHeldInTrust<br> Savings<br> TrustAccounts<br> **Available with minor version: 13**<br> CashAndCashEquivalents<br> OtherEarMarkedBankAccounts<br> |
| Other Current Asset | **Default**<br> AllowanceForBadDebts<br> DevelopmentCosts<br> EmployeeCashAdvances (default)<br> OtherCurrentAssets<br> Inventory<br> Investment_MortgageRealEstateLoans<br> Investment_Other<br> Investment_TaxExemptSecurities<br> Investment_USGovernmentObligations<br> LoansToOfficers<br> LoansToOthers<br> LoansToStockholders<br> PrepaidExpenses<br> Retainage<br> UndepositedFunds<br> **Available with minor version: 13**<br> AssetsAvailableForSale<br> BalWithGovtAuthorities<br> CalledUpShareCapitalNotPaid<br> ExpenditureAuthorisationsAndLettersOfCredit<br> GlobalTaxDeferred<br> GlobalTaxRefund<br> InternalTransfers<br> OtherConsumables<br> ProvisionsCurrentAssets<br> ShortTermInvestmentsInRelatedParties<br> ShortTermLoansAndAdvancesToRelatedParties<br> TradeAndOtherReceivables<br> |
| Fixed Asset | **Default**<br> AccumulatedDepletion<br> AccumulatedDepreciation<br> DepletableAssets<br> FixedAssetComputers<br> FixedAssetCopiers<br> FixedAssetFurniture<br> FixedAssetPhone<br> FixedAssetPhotoVideo<br> FixedAssetSoftware<br> FixedAssetOtherToolsEquipment<br> FurnitureAndFixtures (default)<br> Land<br> LeaseholdImprovements<br> OtherFixedAssets<br> AccumulatedAmortization<br> Buildings<br> IntangibleAssets<br> MachineryAndEquipment<br> Vehicles<br> **Available with minor version: 13**<br> AssetsInCourseOfConstruction<br> CapitalWip<br> CumulativeDepreciationOnIntangibleAssets<br> IntangibleAssetsUnderDevelopment<br> LandAsset<br> NonCurrentAssets<br> ParticipatingInterests<br> ProvisionsFixedAssets<br> |
| Other Asset | **Default**<br> LeaseBuyout<br> OtherLongTermAssets<br> SecurityDeposits<br> AccumulatedAmortizationOfOtherAssets<br> Goodwill<br> Licenses (default)<br> OrganizationalCosts<br> **Available with minor version: 13**<br> AssetsHeldForSale<br> AvailableForSaleFinancialAssets<br> DeferredTax<br> Investments<br> LongTermInvestments<br> LongTermLoansAndAdvancesToRelatedParties<br> OtherIntangibleAssets<br> OtherLongTermInvestments<br> OtherLongTermLoansAndAdvances<br> PrepaymentsAndAccruedIncome<br> ProvisionsNonCurrentAssets<br> |
| Accounts Receivable | **Default**<br> Accounts Receivable<br> |

#### EQUITY

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Equity | **Default** <br> OpeningBalanceEquity (default)<br> PartnersEquity<br> RetainedEarnings<br> AccumulatedAdjustment<br> OwnersEquity<br> PaidInCapitalOrSurplus<br> ​PartnerContributions<br> PartnerDistributions<br> PreferredStock<br> CommonStock<br> TreasuryStock<br> EstimatedTaxes<br> Healthcare<br> PersonalIncome<br> PersonalExpense<br> **Available with minor version: 13**<br> AccumulatedOtherComprehensiveIncome<br> CalledUpShareCapital<br> CapitalReserves<br> DividendDisbursed<br> EquityInEarningsOfSubsiduaries<br> InvestmentGrants<br> MoneyReceivedAgainstShareWarrants<br> OtherFreeReserves<br> ShareApplicationMoneyPendingAllotment<br> ShareCapital<br> Funds<br> |

#### EXPENSE

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Expense | **Default** <br> AdvertisingPromotional<br> BadDebts<br> BankCharges<br> CharitableContributions<br> CommissionsAndFees<br> Entertainment<br> EntertainmentMeals<br> EquipmentRental<br> FinanceCosts<br> GlobalTaxExpense<br> Insurance<br> InterestPaid<br> LegalProfessionalFees<br> OfficeExpenses<br> OfficeGeneralAdministrativeExpenses<br> OtherBusinessExpenses<br> OtherMiscellaneousServiceCost<br> PromotionalMeals<br> RentOrLeaseOfBuildings<br> RepairMaintenance<br> ShippingFreightDelivery<br> SuppliesMaterials<br> Travel (default)<br> TravelMeals<br> Utilities<br> Auto<br> CostOfLabor<br> DuesSubscriptions<br> PayrollExpenses<br> TaxesPaid<br> UnappliedCashBillPaymentExpense<br> Utilities<br> **Available with minor version: 13**<br> AmortizationExpense<br> AppropriationsToDepreciation<br> BorrowingCost<br> CommissionsAndFees<br> DistributionCosts<br> ExternalServices<br> ExtraordinaryCharges<br> IncomeTaxExpense<br> LossOnDiscontinuedOperationsNetOfTax<br> ManagementCompensation<br> OtherCurrentOperatingCharges<br> OtherExternalServices<br> OtherRentalCosts<br> OtherSellingExpenses<br> ProjectStudiesSurveysAssessments<br> PurchasesRebates<br> ShippingAndDeliveryExpense<br> StaffCosts<br> Sundry<br> TravelExpensesGeneralAndAdminExpenses<br> TravelExpensesSellingExpense<br> |
| Other Expense | **Default**<br> Depreciation (default)<br> ExchangeGainOrLoss<br> OtherMiscellaneousExpense<br> PenaltiesSettlements<br> Amortization<br> GasAndFuel<br> HomeOffice<br> HomeOwnerRentalInsurance<br> OtherHomeOfficeExpenses<br> MortgageInterest<br> RentAndLease<br> RepairsAndMaintenance<br> ParkingAndTolls<br> Vehicle<br> VehicleInsurance<br> VehicleLease<br> VehicleLoanInterest<br> VehicleLoan<br> VehicleRegistration<br> VehicleRepairs<br> OtherVehicleExpenses<br> Utilities<br> WashAndRoadServices <br> **Available with minor version: 13**<br> DeferredTaxExpense<br> Depletion<br> ExceptionalItems<br> ExtraordinaryItems<br> IncomeTaxOtherExpense<br> MatCredit<br> PriorPeriodItems<br> TaxRoundoffGainOrLoss<br> |
| Cost of Goods Sold | **Default**<br> EquipmentRentalCos<br> OtherCostsOfServiceCos<br> ShippingFreightDeliveryCos<br> SuppliesMaterialsCogs<br> CostOfLaborCos (default)<br> **Available with minor version: 13**<br> CostOfSales<br> FreightAndDeliveryCost<br> |

#### LIABILITY

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Accounts Payable | **Default** <br> Accounts Payable<br> **Available with minor version: 13**<br> OutstandingDuesMicroSmallEnterprise<br> OutstandingDuesOtherThanMicroSmallEnterprise<br> |
| Credit Card | **Default**<br> Credit Card <br> |
| Long Term Liability | **Default**<br> NotesPayable (default)<br> OtherLongTermLiabilities<br> ShareholderNotesPayable<br> **Available with minor version: 13**<br> AccrualsAndDeferredIncome<br> AccruedLongLermLiabilities<br> AccruedVacationPayable<br> BankLoans<br> DebtsRelatedToParticipatingInterests<br> DeferredTaxLiabilities<br> GovernmentAndOtherPublicAuthorities<br> GroupAndAssociates<br> LiabilitiesRelatedToAssetsHeldForSale<br> LongTermBorrowings<br> LongTermDebit<br> LongTermEmployeeBenefitObligations<br> ObligationsUnderFinanceLeases<br> OtherLongTermProvisions<br> ProvisionForLiabilities<br> ProvisionsNonCurrentLiabilities<br> StaffAndRelatedLongTermLiabilityAccounts<br> |
| Other Current Liability | **Default**<br> DirectDepositPayable<br> LineOfCredit<br> LoanPayable<br> GlobalTaxPayable<br> GlobalTaxSuspense<br> OtherCurrentLiabilities (default)<br> PayrollClearing<br> PayrollTaxPayable<br> PrepaidExpensesPayable<br> RentsInTrustLiability<br> TrustAccountsLiabilities<br> FederalIncomeTaxPayable<br> InsurancePayable<br> SalesTaxPayable<br> StateLocalIncomeTaxPayable <br> **Available with minor version: 13**<br> AccruedLiabilities<br> CurrentLiabilities<br> CurrentPortionEmployeeBenefitsObligations<br> CurrentPortionOfObligationsUnderFinanceLeases<br> CurrentTaxLiability<br> DividendsPayable<br> DutiesAndTaxes<br> InterestPayables<br> ProvisionForWarrantyObligations<br> ProvisionsCurrentLiabilities<br> ShortTermBorrowings<br> SocialSecurityAgencies<br> StaffAndRelatedLiabilityAccounts<br> SundryDebtorsAndCreditors<br> TradeAndOtherPayables<br> |

#### REVENUE

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Income | **Default** <br> NonProfitIncome<br> OtherPrimaryIncome (default)<br> SalesOfProductIncome<br> ServiceFeeIncome<br> DiscountsRefundsGiven<br> UnappliedCashPaymentIncome<br> **Available with minor version: 13**<br> CashReceiptIncome<br> OperatingGrants<br> OtherCurrentOperatingIncome<br> OwnWorkCapitalized<br> RevenueGeneral<br> SalesRetail<br> SalesWholesale<br> SavingsByTaxScheme<br> |
| Other Income | **Default**<br> DividendIncome<br> InterestEarned<br> OtherInvestmentIncome (default)<br> OtherMiscellaneousIncome<br> TaxExemptInterest <br> **Available with minor version: 13**<br> GainLossOnSaleOfFixedAssets<br> GainLossOnSaleOfInvestments<br> LossOnDisposalOfAssets<br> OtherOperatingIncome<br> UnrealisedLossOnSecuritiesNetOfTax<br> |

</details>

##### `AccountSubType`

Required: Conditionally required
Type: `String`
Traits: filterable

The account sub-type classification and is based on the AccountType value.
 Required if AccountType is not specified.

<details>
<summary>Show child attributes</summary>

#### ASSET

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Bank | **Default**<br> CashOnHand (default)<br> Checking <br> MoneyMarket<br> RentsHeldInTrust<br> Savings<br> TrustAccounts<br> **Available with minor version: 13**<br> CashAndCashEquivalents<br> OtherEarMarkedBankAccounts<br> |
| Other Current Asset | **Default**<br> AllowanceForBadDebts<br> DevelopmentCosts<br> EmployeeCashAdvances (default)<br> OtherCurrentAssets<br> Inventory<br> Investment_MortgageRealEstateLoans<br> Investment_Other<br> Investment_TaxExemptSecurities<br> Investment_USGovernmentObligations<br> LoansToOfficers<br> LoansToOthers<br> LoansToStockholders<br> PrepaidExpenses<br> Retainage<br> UndepositedFunds<br> **Available with minor version: 13**<br> AssetsAvailableForSale<br> BalWithGovtAuthorities<br> CalledUpShareCapitalNotPaid<br> ExpenditureAuthorisationsAndLettersOfCredit<br> GlobalTaxDeferred<br> GlobalTaxRefund<br> InternalTransfers<br> OtherConsumables<br> ProvisionsCurrentAssets<br> ShortTermInvestmentsInRelatedParties<br> ShortTermLoansAndAdvancesToRelatedParties<br> TradeAndOtherReceivables<br> |
| Fixed Asset | **Default**<br> AccumulatedDepletion<br> AccumulatedDepreciation<br> DepletableAssets<br> FixedAssetComputers<br> FixedAssetCopiers<br> FixedAssetFurniture<br> FixedAssetPhone<br> FixedAssetPhotoVideo<br> FixedAssetSoftware<br> FixedAssetOtherToolsEquipment<br> FurnitureAndFixtures (default)<br> Land<br> LeaseholdImprovements<br> OtherFixedAssets<br> AccumulatedAmortization<br> Buildings<br> IntangibleAssets<br> MachineryAndEquipment<br> Vehicles<br> **Available with minor version: 13**<br> AssetsInCourseOfConstruction<br> CapitalWip<br> CumulativeDepreciationOnIntangibleAssets<br> IntangibleAssetsUnderDevelopment<br> LandAsset<br> NonCurrentAssets<br> ParticipatingInterests<br> ProvisionsFixedAssets<br> |
| Other Asset | **Default**<br> LeaseBuyout<br> OtherLongTermAssets<br> SecurityDeposits<br> AccumulatedAmortizationOfOtherAssets<br> Goodwill<br> Licenses (default)<br> OrganizationalCosts<br> **Available with minor version: 13**<br> AssetsHeldForSale<br> AvailableForSaleFinancialAssets<br> DeferredTax<br> Investments<br> LongTermInvestments<br> LongTermLoansAndAdvancesToRelatedParties<br> OtherIntangibleAssets<br> OtherLongTermInvestments<br> OtherLongTermLoansAndAdvances<br> PrepaymentsAndAccruedIncome<br> ProvisionsNonCurrentAssets<br> |
| Accounts Receivable | **Default**<br> Accounts Receivable<br> |

#### EQUITY

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Equity | **Default** <br> OpeningBalanceEquity (default)<br> PartnersEquity<br> RetainedEarnings<br> AccumulatedAdjustment<br> OwnersEquity<br> PaidInCapitalOrSurplus<br> ​PartnerContributions<br> PartnerDistributions<br> PreferredStock<br> CommonStock<br> TreasuryStock<br> EstimatedTaxes<br> Healthcare<br> PersonalIncome<br> PersonalExpense<br> **Available with minor version: 13**<br> AccumulatedOtherComprehensiveIncome<br> CalledUpShareCapital<br> CapitalReserves<br> DividendDisbursed<br> EquityInEarningsOfSubsiduaries<br> InvestmentGrants<br> MoneyReceivedAgainstShareWarrants<br> OtherFreeReserves<br> ShareApplicationMoneyPendingAllotment<br> ShareCapital<br> Funds<br> |

#### EXPENSE

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Expense | **Default** <br> AdvertisingPromotional<br> BadDebts<br> BankCharges<br> CharitableContributions<br> CommissionsAndFees<br> Entertainment<br> EntertainmentMeals<br> EquipmentRental<br> FinanceCosts<br> GlobalTaxExpense<br> Insurance<br> InterestPaid<br> LegalProfessionalFees<br> OfficeExpenses<br> OfficeGeneralAdministrativeExpenses<br> OtherBusinessExpenses<br> OtherMiscellaneousServiceCost<br> PromotionalMeals<br> RentOrLeaseOfBuildings<br> RepairMaintenance<br> ShippingFreightDelivery<br> SuppliesMaterials<br> Travel (default)<br> TravelMeals<br> Utilities<br> Auto<br> CostOfLabor<br> DuesSubscriptions<br> PayrollExpenses<br> TaxesPaid<br> UnappliedCashBillPaymentExpense<br> Utilities<br> **Available with minor version: 13**<br> AmortizationExpense<br> AppropriationsToDepreciation<br> BorrowingCost<br> CommissionsAndFees<br> DistributionCosts<br> ExternalServices<br> ExtraordinaryCharges<br> IncomeTaxExpense<br> LossOnDiscontinuedOperationsNetOfTax<br> ManagementCompensation<br> OtherCurrentOperatingCharges<br> OtherExternalServices<br> OtherRentalCosts<br> OtherSellingExpenses<br> ProjectStudiesSurveysAssessments<br> PurchasesRebates<br> ShippingAndDeliveryExpense<br> StaffCosts<br> Sundry<br> TravelExpensesGeneralAndAdminExpenses<br> TravelExpensesSellingExpense<br> |
| Other Expense | **Default**<br> Depreciation (default)<br> ExchangeGainOrLoss<br> OtherMiscellaneousExpense<br> PenaltiesSettlements<br> Amortization<br> GasAndFuel<br> HomeOffice<br> HomeOwnerRentalInsurance<br> OtherHomeOfficeExpenses<br> MortgageInterest<br> RentAndLease<br> RepairsAndMaintenance<br> ParkingAndTolls<br> Vehicle<br> VehicleInsurance<br> VehicleLease<br> VehicleLoanInterest<br> VehicleLoan<br> VehicleRegistration<br> VehicleRepairs<br> OtherVehicleExpenses<br> Utilities<br> WashAndRoadServices <br> **Available with minor version: 13**<br> DeferredTaxExpense<br> Depletion<br> ExceptionalItems<br> ExtraordinaryItems<br> IncomeTaxOtherExpense<br> MatCredit<br> PriorPeriodItems<br> TaxRoundoffGainOrLoss<br> |
| Cost of Goods Sold | **Default**<br> EquipmentRentalCos<br> OtherCostsOfServiceCos<br> ShippingFreightDeliveryCos<br> SuppliesMaterialsCogs<br> CostOfLaborCos (default)<br> **Available with minor version: 13**<br> CostOfSales<br> FreightAndDeliveryCost<br> |

#### LIABILITY

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Accounts Payable | **Default** <br> Accounts Payable<br> **Available with minor version: 13**<br> OutstandingDuesMicroSmallEnterprise<br> OutstandingDuesOtherThanMicroSmallEnterprise<br> |
| Credit Card | **Default**<br> Credit Card <br> |
| Long Term Liability | **Default**<br> NotesPayable (default)<br> OtherLongTermLiabilities<br> ShareholderNotesPayable<br> **Available with minor version: 13**<br> AccrualsAndDeferredIncome<br> AccruedLongLermLiabilities<br> AccruedVacationPayable<br> BankLoans<br> DebtsRelatedToParticipatingInterests<br> DeferredTaxLiabilities<br> GovernmentAndOtherPublicAuthorities<br> GroupAndAssociates<br> LiabilitiesRelatedToAssetsHeldForSale<br> LongTermBorrowings<br> LongTermDebit<br> LongTermEmployeeBenefitObligations<br> ObligationsUnderFinanceLeases<br> OtherLongTermProvisions<br> ProvisionForLiabilities<br> ProvisionsNonCurrentLiabilities<br> StaffAndRelatedLongTermLiabilityAccounts<br> |
| Other Current Liability | **Default**<br> DirectDepositPayable<br> LineOfCredit<br> LoanPayable<br> GlobalTaxPayable<br> GlobalTaxSuspense<br> OtherCurrentLiabilities (default)<br> PayrollClearing<br> PayrollTaxPayable<br> PrepaidExpensesPayable<br> RentsInTrustLiability<br> TrustAccountsLiabilities<br> FederalIncomeTaxPayable<br> InsurancePayable<br> SalesTaxPayable<br> StateLocalIncomeTaxPayable <br> **Available with minor version: 13**<br> AccruedLiabilities<br> CurrentLiabilities<br> CurrentPortionEmployeeBenefitsObligations<br> CurrentPortionOfObligationsUnderFinanceLeases<br> CurrentTaxLiability<br> DividendsPayable<br> DutiesAndTaxes<br> InterestPayables<br> ProvisionForWarrantyObligations<br> ProvisionsCurrentLiabilities<br> ShortTermBorrowings<br> SocialSecurityAgencies<br> StaffAndRelatedLiabilityAccounts<br> SundryDebtorsAndCreditors<br> TradeAndOtherPayables<br> |

#### REVENUE

| Name | Description |
| --- | --- |
| **ACCOUNT TYPE** | **ACCOUNT SUB TYPE** |
| Income | **Default** <br> NonProfitIncome<br> OtherPrimaryIncome (default)<br> SalesOfProductIncome<br> ServiceFeeIncome<br> DiscountsRefundsGiven<br> UnappliedCashPaymentIncome<br> **Available with minor version: 13**<br> CashReceiptIncome<br> OperatingGrants<br> OtherCurrentOperatingIncome<br> OwnWorkCapitalized<br> RevenueGeneral<br> SalesRetail<br> SalesWholesale<br> SavingsByTaxScheme<br> |
| Other Income | **Default**<br> DividendIncome<br> InterestEarned<br> OtherInvestmentIncome (default)<br> OtherMiscellaneousIncome<br> TaxExemptInterest <br> **Available with minor version: 13**<br> GainLossOnSaleOfFixedAssets<br> GainLossOnSaleOfInvestments<br> LossOnDisposalOfAssets<br> OtherOperatingIncome<br> UnrealisedLossOnSecuritiesNetOfTax<br> |

</details>

</details>

#### Example

```json
{
  "Name": "MyJobs_test",
  "AccountType": "Accounts Receivable"
}
```

#### XML example

```xml
<Account xmlns="http://schema.intuit.com/finance/v3">
  <Name>MyClients</Name>
  <!--change name if the request fails with 400 due to Duplicate name-->
  <AccountType>Accounts Receivable</AccountType>
</Account>
```

### Returns

Returns the newly created Account object.

#### Example

```json
{
  "Account": {
    "FullyQualifiedName": "MyJobs",
    "domain": "QBO",
    "Name": "MyJobs",
    "Classification": "Asset",
    "AccountSubType": "AccountsReceivable",
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "CurrentBalanceWithSubAccounts": 0,
    "sparse": false,
    "MetaData": {
      "CreateTime": "2014-12-31T09:29:05-08:00",
      "LastUpdatedTime": "2014-12-31T09:29:05-08:00"
    },
    "AccountType": "Accounts Receivable",
    "CurrentBalance": 0,
    "Active": true,
    "SyncToken": "0",
    "Id": "94",
    "SubAccount": false
  },
  "time": "2014-12-31T09:29:05.717-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-13T12:30:07.458-07:00">
  <Account domain="QBO" sparse="false">
    <Id>93</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-07-13T12:34:47-07:00</CreateTime>
      <LastUpdatedTime>2015-07-13T12:34:47-07:00</LastUpdatedTime>
    </MetaData>
    <Name>MyClients</Name>
    <SubAccount>false</SubAccount>
    <FullyQualifiedName>MyClients</FullyQualifiedName>
    <Active>true</Active>
    <Classification>Asset</Classification>
    <AccountType>Accounts Receivable</AccountType>
    <AccountSubType>AccountsReceivable</AccountSubType>
    <CurrentBalance>0</CurrentBalance>
    <CurrentBalanceWithSubAccounts>0</CurrentBalanceWithSubAccounts>
    <CurrencyRef name="United States Dollar">USD</CurrencyRef>
  </Account>
</IntuitResponse>
```

## Query an account

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from Account where Metadata.CreateTime > '2014-12-31'"
```

#### XML example

```sql
select * from Account where Metadata.CreateTime > '2014-12-31'
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "Account": [
      {
        "FullyQualifiedName": "Canadian Accounts Receivable",
        "domain": "QBO",
        "Name": "Canadian Accounts Receivable",
        "Classification": "Asset",
        "AccountSubType": "AccountsReceivable",
        "CurrencyRef": {
          "name": "United States Dollar",
          "value": "USD"
        },
        "CurrentBalanceWithSubAccounts": 0,
        "sparse": false,
        "MetaData": {
          "CreateTime": "2015-06-23T09:38:18-07:00",
          "LastUpdatedTime": "2015-06-23T09:38:18-07:00"
        },
        "AccountType": "Accounts Receivable",
        "CurrentBalance": 0,
        "Active": true,
        "SyncToken": "0",
        "Id": "92",
        "SubAccount": false
      },
      {
        "FullyQualifiedName": "MyClients",
        "domain": "QBO",
        "Name": "MyClients",
        "Classification": "Asset",
        "AccountSubType": "AccountsReceivable",
        "CurrencyRef": {
          "name": "United States Dollar",
          "value": "USD"
        },
        "CurrentBalanceWithSubAccounts": 0,
        "sparse": false,
        "MetaData": {
          "CreateTime": "2015-07-13T12:34:47-07:00",
          "LastUpdatedTime": "2015-07-13T12:34:47-07:00"
        },
        "AccountType": "Accounts Receivable",
        "CurrentBalance": 0,
        "Active": true,
        "SyncToken": "0",
        "Id": "93",
        "SubAccount": false
      },
      {
        "FullyQualifiedName": "MyJobs",
        "domain": "QBO",
        "Name": "MyJobs",
        "Classification": "Asset",
        "AccountSubType": "AccountsReceivable",
        "CurrencyRef": {
          "name": "United States Dollar",
          "value": "USD"
        },
        "CurrentBalanceWithSubAccounts": 0,
        "sparse": false,
        "MetaData": {
          "CreateTime": "2015-01-13T10:29:27-08:00",
          "LastUpdatedTime": "2015-01-13T10:29:27-08:00"
        },
        "AccountType": "Accounts Receivable",
        "CurrentBalance": 0,
        "Active": true,
        "SyncToken": "0",
        "Id": "91",
        "SubAccount": false
      }
    ],
    "maxResults": 3
  },
  "time": "2015-07-13T12:35:57.651-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-13T12:35:07.060-07:00">
    <QueryResponse startPosition="1" maxResults="3">
        <Account domain="QBO" sparse="false">
            <Id>92</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-06-23T09:38:18-07:00</CreateTime>
                <LastUpdatedTime>2015-06-23T09:38:18-07:00</LastUpdatedTime>
            </MetaData>
            <Name>Canadian Accounts Receivable</Name>
            <SubAccount>false</SubAccount>
            <FullyQualifiedName>Canadian Accounts Receivable</FullyQualifiedName>
            <Active>true</Active>
            <Classification>Asset</Classification>
            <AccountType>Accounts Receivable</AccountType>
            <AccountSubType>AccountsReceivable</AccountSubType>
            <CurrentBalance>0</CurrentBalance>
            <CurrentBalanceWithSubAccounts>0</CurrentBalanceWithSubAccounts>
            <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        </Account>
        <Account domain="QBO" sparse="false">
            <Id>93</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-07-13T12:34:47-07:00</CreateTime>
                <LastUpdatedTime>2015-07-13T12:34:47-07:00</LastUpdatedTime>
            </MetaData>
            <Name>MyClients</Name>
            <SubAccount>false</SubAccount>
            <FullyQualifiedName>MyClients</FullyQualifiedName>
            <Active>true</Active>
            <Classification>Asset</Classification>
            <AccountType>Accounts Receivable</AccountType>
            <AccountSubType>AccountsReceivable</AccountSubType>
            <CurrentBalance>0</CurrentBalance>
            <CurrentBalanceWithSubAccounts>0</CurrentBalanceWithSubAccounts>
            <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        </Account>
        <Account domain="QBO" sparse="false">
            <Id>91</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-01-13T10:29:27-08:00</CreateTime>
                <LastUpdatedTime>2015-01-13T10:29:27-08:00</LastUpdatedTime>
            </MetaData>
            <Name>MyJobs</Name>
            <SubAccount>false</SubAccount>
            <FullyQualifiedName>MyJobs</FullyQualifiedName>
            <Active>true</Active>
            <Classification>Asset</Classification>
            <AccountType>Accounts Receivable</AccountType>
            <AccountSubType>AccountsReceivable</AccountSubType>
            <CurrentBalance>0</CurrentBalance>
            <CurrentBalanceWithSubAccounts>0</CurrentBalanceWithSubAccounts>
            <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        </Account>
    </QueryResponse>
</IntuitResponse>
```

## Read an account

### Definition

- **Operation:** `GET /v3/company/<realmID>/account/<accountId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of an Account object that has been previously created.

### Returns

Returns the Account object.

#### Example

```json
{
  "Account": {
    "FullyQualifiedName": "Accounts Payable (A/P)",
    "domain": "QBO",
    "Name": "Accounts Payable (A/P)",
    "Classification": "Liability",
    "AccountSubType": "AccountsPayable",
    "CurrentBalanceWithSubAccounts": -1091.23,
    "sparse": false,
    "MetaData": {
      "CreateTime": "2014-09-12T10:12:02-07:00",
      "LastUpdatedTime": "2015-06-30T15:09:07-07:00"
    },
    "AccountType": "Accounts Payable",
    "CurrentBalance": -1091.23,
    "Active": true,
    "SyncToken": "0",
    "Id": "33",
    "SubAccount": false
  },
  "time": "2015-07-13T12:50:36.72-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-13T12:51:18.467-07:00">
  <Account domain="QBO" sparse="false">
    <Id>33</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2014-09-12T10:12:02-07:00</CreateTime>
      <LastUpdatedTime>2015-06-30T15:09:07-07:00</LastUpdatedTime>
    </MetaData>
    <Name>Accounts Payable (A/P)</Name>
    <SubAccount>false</SubAccount>
    <FullyQualifiedName>Accounts Payable (A/P)</FullyQualifiedName>
    <Active>true</Active>
    <Classification>Liability</Classification>
    <AccountType>Accounts Payable</AccountType>
    <AccountSubType>AccountsPayable</AccountSubType>
    <CurrentBalance>-1091.23</CurrentBalance>
    <CurrentBalanceWithSubAccounts>-1091.23</CurrentBalanceWithSubAccounts>
  </Account>
</IntuitResponse>
```

## Full update an account

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/account`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing account object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `accountresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "FullyQualifiedName": "Accounts Payable (A/P)",
  "domain": "QBO",
  "SubAccount": false,
  "Description": "Description added during update.",
  "Classification": "Liability",
  "AccountSubType": "AccountsPayable",
  "CurrentBalanceWithSubAccounts": -1091.23,
  "sparse": false,
  "MetaData": {
    "CreateTime": "2014-09-12T10:12:02-07:00",
    "LastUpdatedTime": "2015-06-30T15:09:07-07:00"
  },
  "AccountType": "Accounts Payable",
  "CurrentBalance": -1091.23,
  "Active": true,
  "SyncToken": "0",
  "Id": "33",
  "Name": "Accounts Payable (A/P)"
}
```

#### XML example

```xml
<Account xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>33</Id>
    <SyncToken>2</SyncToken>
    <MetaData>
      <CreateTime>2014-09-12T10:12:02-07:00</CreateTime>
      <LastUpdatedTime>2015-07-13T15:35:13-07:00</LastUpdatedTime>
    </MetaData>
    <Name>Accounts Payable (A/P)</Name>
    <SubAccount>false</SubAccount>
    <Description>Another description update.</Description>
    <FullyQualifiedName>Accounts Payable (A/P)</FullyQualifiedName>
    <Active>true</Active>
    <Classification>Liability</Classification>
    <AccountType>Accounts Payable</AccountType>
    <AccountSubType>AccountsPayable</AccountSubType>
    <CurrentBalance>-1091.23</CurrentBalance>
    <CurrentBalanceWithSubAccounts>-1091.23</CurrentBalanceWithSubAccounts>
</Account>
```

### Returns

The account response body.

#### Example

```json
{
  "Account": {
    "FullyQualifiedName": "Accounts Payable (A/P)",
    "domain": "QBO",
    "SubAccount": false,
    "Description": "Description added during update.",
    "Classification": "Liability",
    "AccountSubType": "AccountsPayable",
    "CurrentBalanceWithSubAccounts": -1091.23,
    "sparse": false,
    "MetaData": {
      "CreateTime": "2014-09-12T10:12:02-07:00",
      "LastUpdatedTime": "2015-07-13T15:35:13-07:00"
    },
    "AccountType": "Accounts Payable",
    "CurrentBalance": -1091.23,
    "Active": true,
    "SyncToken": "1",
    "Id": "33",
    "Name": "Accounts Payable (A/P)"
  },
  "time": "2015-07-13T15:31:25.618-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-13T15:46:56.803-07:00">
  <Account domain="QBO" sparse="false">
    <Id>33</Id>
    <SyncToken>3</SyncToken>
    <MetaData>
      <CreateTime>2014-09-12T10:12:02-07:00</CreateTime>
      <LastUpdatedTime>2015-07-13T15:50:44-07:00</LastUpdatedTime>
    </MetaData>
    <Name>Accounts Payable (A/P)</Name>
    <SubAccount>false</SubAccount>
    <Description>Another description update.</Description>
    <FullyQualifiedName>Accounts Payable (A/P)</FullyQualifiedName>
    <Active>true</Active>
    <Classification>Liability</Classification>
    <AccountType>Accounts Payable</AccountType>
    <AccountSubType>AccountsPayable</AccountSubType>
    <CurrentBalance>-1091.23</CurrentBalance>
    <CurrentBalanceWithSubAccounts>-1091.23</CurrentBalanceWithSubAccounts>
  </Account>
</IntuitResponse>
```
