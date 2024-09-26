# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: FedCm (experimental)

from __future__ import annotations
import enum
import typing
from dataclasses import dataclass
from .util import event_class, T_JSON_DICT


class LoginState(enum.Enum):
    """
    Whether this is a sign-up or sign-in action for this account, i.e.
    whether this account has ever been used to sign in to this RP before.
    """

    SIGN_IN = "SignIn"
    SIGN_UP = "SignUp"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> LoginState:
        return cls(json)


class DialogType(enum.Enum):
    """
    The types of FedCM dialogs.
    """

    ACCOUNT_CHOOSER = "AccountChooser"
    AUTO_REAUTHN = "AutoReauthn"
    CONFIRM_IDP_LOGIN = "ConfirmIdpLogin"
    ERROR = "Error"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> DialogType:
        return cls(json)


class DialogButton(enum.Enum):
    """
    The buttons on the FedCM dialog.
    """

    CONFIRM_IDP_LOGIN_CONTINUE = "ConfirmIdpLoginContinue"
    ERROR_GOT_IT = "ErrorGotIt"
    ERROR_MORE_DETAILS = "ErrorMoreDetails"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> DialogButton:
        return cls(json)


class AccountUrlType(enum.Enum):
    """
    The URLs that each account has
    """

    TERMS_OF_SERVICE = "TermsOfService"
    PRIVACY_POLICY = "PrivacyPolicy"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> AccountUrlType:
        return cls(json)


@dataclass
class Account:
    """
    Corresponds to IdentityRequestAccount
    """

    account_id: str

    email: str

    name: str

    given_name: str

    picture_url: str

    idp_config_url: str

    idp_login_url: str

    login_state: LoginState

    #: These two are only set if the loginState is signUp
    terms_of_service_url: typing.Optional[str] = None

    privacy_policy_url: typing.Optional[str] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["accountId"] = self.account_id
        json["email"] = self.email
        json["name"] = self.name
        json["givenName"] = self.given_name
        json["pictureUrl"] = self.picture_url
        json["idpConfigUrl"] = self.idp_config_url
        json["idpLoginUrl"] = self.idp_login_url
        json["loginState"] = self.login_state.to_json()
        if self.terms_of_service_url is not None:
            json["termsOfServiceUrl"] = self.terms_of_service_url
        if self.privacy_policy_url is not None:
            json["privacyPolicyUrl"] = self.privacy_policy_url
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> Account:
        return cls(
            account_id=str(json["accountId"]),
            email=str(json["email"]),
            name=str(json["name"]),
            given_name=str(json["givenName"]),
            picture_url=str(json["pictureUrl"]),
            idp_config_url=str(json["idpConfigUrl"]),
            idp_login_url=str(json["idpLoginUrl"]),
            login_state=LoginState.from_json(json["loginState"]),
            terms_of_service_url=(
                str(json["termsOfServiceUrl"])
                if json.get("termsOfServiceUrl", None) is not None
                else None
            ),
            privacy_policy_url=(
                str(json["privacyPolicyUrl"])
                if json.get("privacyPolicyUrl", None) is not None
                else None
            ),
        )


def enable(
    disable_rejection_delay: typing.Optional[bool] = None,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    :param disable_rejection_delay: *(Optional)* Allows callers to disable the promise rejection delay that would normally happen, if this is unimportant to what's being tested. (step 4 of https://fedidcg.github.io/FedCM/#browser-api-rp-sign-in)
    """
    params: T_JSON_DICT = dict()
    if disable_rejection_delay is not None:
        params["disableRejectionDelay"] = disable_rejection_delay
    cmd_dict: T_JSON_DICT = {
        "method": "FedCm.enable",
        "params": params,
    }
    json = yield cmd_dict


def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:

    cmd_dict: T_JSON_DICT = {
        "method": "FedCm.disable",
    }
    json = yield cmd_dict


def select_account(
    dialog_id: str, account_index: int
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    :param dialog_id:
    :param account_index:
    """
    params: T_JSON_DICT = dict()
    params["dialogId"] = dialog_id
    params["accountIndex"] = account_index
    cmd_dict: T_JSON_DICT = {
        "method": "FedCm.selectAccount",
        "params": params,
    }
    json = yield cmd_dict


def click_dialog_button(
    dialog_id: str, dialog_button: DialogButton
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    :param dialog_id:
    :param dialog_button:
    """
    params: T_JSON_DICT = dict()
    params["dialogId"] = dialog_id
    params["dialogButton"] = dialog_button.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "FedCm.clickDialogButton",
        "params": params,
    }
    json = yield cmd_dict


def open_url(
    dialog_id: str, account_index: int, account_url_type: AccountUrlType
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    :param dialog_id:
    :param account_index:
    :param account_url_type:
    """
    params: T_JSON_DICT = dict()
    params["dialogId"] = dialog_id
    params["accountIndex"] = account_index
    params["accountUrlType"] = account_url_type.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "FedCm.openUrl",
        "params": params,
    }
    json = yield cmd_dict


def dismiss_dialog(
    dialog_id: str, trigger_cooldown: typing.Optional[bool] = None
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    :param dialog_id:
    :param trigger_cooldown: *(Optional)*
    """
    params: T_JSON_DICT = dict()
    params["dialogId"] = dialog_id
    if trigger_cooldown is not None:
        params["triggerCooldown"] = trigger_cooldown
    cmd_dict: T_JSON_DICT = {
        "method": "FedCm.dismissDialog",
        "params": params,
    }
    json = yield cmd_dict


def reset_cooldown() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Resets the cooldown time, if any, to allow the next FedCM call to show
    a dialog even if one was recently dismissed by the user.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "FedCm.resetCooldown",
    }
    json = yield cmd_dict


@event_class("FedCm.dialogShown")
@dataclass
class DialogShown:
    dialog_id: str
    dialog_type: DialogType
    accounts: typing.List[Account]
    #: These exist primarily so that the caller can verify the
    #: RP context was used appropriately.
    title: str
    subtitle: typing.Optional[str]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> DialogShown:
        return cls(
            dialog_id=str(json["dialogId"]),
            dialog_type=DialogType.from_json(json["dialogType"]),
            accounts=[Account.from_json(i) for i in json["accounts"]],
            title=str(json["title"]),
            subtitle=(
                str(json["subtitle"])
                if json.get("subtitle", None) is not None
                else None
            ),
        )


@event_class("FedCm.dialogClosed")
@dataclass
class DialogClosed:
    """
    Triggered when a dialog is closed, either by user action, JS abort,
    or a command below.
    """

    dialog_id: str

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> DialogClosed:
        return cls(dialog_id=str(json["dialogId"]))
