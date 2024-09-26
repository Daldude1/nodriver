# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: Animation (experimental)

from __future__ import annotations
import enum
import typing
from dataclasses import dataclass
from .util import event_class, T_JSON_DICT

from . import dom
from . import runtime


@dataclass
class Animation:
    """
    Animation instance.
    """

    #: ``Animation``'s id.
    id_: str

    #: ``Animation``'s name.
    name: str

    #: ``Animation``'s internal paused state.
    paused_state: bool

    #: ``Animation``'s play state.
    play_state: str

    #: ``Animation``'s playback rate.
    playback_rate: float

    #: ``Animation``'s start time.
    #: Milliseconds for time based animations and
    #: percentage [0 - 100] for scroll driven animations
    #: (i.e. when viewOrScrollTimeline exists).
    start_time: float

    #: ``Animation``'s current time.
    current_time: float

    #: Animation type of ``Animation``.
    type_: str

    #: ``Animation``'s source animation node.
    source: typing.Optional[AnimationEffect] = None

    #: A unique ID for ``Animation`` representing the sources that triggered this CSS
    #: animation/transition.
    css_id: typing.Optional[str] = None

    #: View or scroll timeline
    view_or_scroll_timeline: typing.Optional[ViewOrScrollTimeline] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["id"] = self.id_
        json["name"] = self.name
        json["pausedState"] = self.paused_state
        json["playState"] = self.play_state
        json["playbackRate"] = self.playback_rate
        json["startTime"] = self.start_time
        json["currentTime"] = self.current_time
        json["type"] = self.type_
        if self.source is not None:
            json["source"] = self.source.to_json()
        if self.css_id is not None:
            json["cssId"] = self.css_id
        if self.view_or_scroll_timeline is not None:
            json["viewOrScrollTimeline"] = self.view_or_scroll_timeline.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> Animation:
        return cls(
            id_=str(json["id"]),
            name=str(json["name"]),
            paused_state=bool(json["pausedState"]),
            play_state=str(json["playState"]),
            playback_rate=float(json["playbackRate"]),
            start_time=float(json["startTime"]),
            current_time=float(json["currentTime"]),
            type_=str(json["type"]),
            source=(
                AnimationEffect.from_json(json["source"])
                if json.get("source", None) is not None
                else None
            ),
            css_id=str(json["cssId"]) if json.get("cssId", None) is not None else None,
            view_or_scroll_timeline=(
                ViewOrScrollTimeline.from_json(json["viewOrScrollTimeline"])
                if json.get("viewOrScrollTimeline", None) is not None
                else None
            ),
        )


@dataclass
class ViewOrScrollTimeline:
    """
    Timeline instance
    """

    #: Orientation of the scroll
    axis: dom.ScrollOrientation

    #: Scroll container node
    source_node_id: typing.Optional[dom.BackendNodeId] = None

    #: Represents the starting scroll position of the timeline
    #: as a length offset in pixels from scroll origin.
    start_offset: typing.Optional[float] = None

    #: Represents the ending scroll position of the timeline
    #: as a length offset in pixels from scroll origin.
    end_offset: typing.Optional[float] = None

    #: The element whose principal box's visibility in the
    #: scrollport defined the progress of the timeline.
    #: Does not exist for animations with ScrollTimeline
    subject_node_id: typing.Optional[dom.BackendNodeId] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["axis"] = self.axis.to_json()
        if self.source_node_id is not None:
            json["sourceNodeId"] = self.source_node_id.to_json()
        if self.start_offset is not None:
            json["startOffset"] = self.start_offset
        if self.end_offset is not None:
            json["endOffset"] = self.end_offset
        if self.subject_node_id is not None:
            json["subjectNodeId"] = self.subject_node_id.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> ViewOrScrollTimeline:
        return cls(
            axis=dom.ScrollOrientation.from_json(json["axis"]),
            source_node_id=(
                dom.BackendNodeId.from_json(json["sourceNodeId"])
                if json.get("sourceNodeId", None) is not None
                else None
            ),
            start_offset=(
                float(json["startOffset"])
                if json.get("startOffset", None) is not None
                else None
            ),
            end_offset=(
                float(json["endOffset"])
                if json.get("endOffset", None) is not None
                else None
            ),
            subject_node_id=(
                dom.BackendNodeId.from_json(json["subjectNodeId"])
                if json.get("subjectNodeId", None) is not None
                else None
            ),
        )


@dataclass
class AnimationEffect:
    """
    AnimationEffect instance
    """

    #: ``AnimationEffect``'s delay.
    delay: float

    #: ``AnimationEffect``'s end delay.
    end_delay: float

    #: ``AnimationEffect``'s iteration start.
    iteration_start: float

    #: ``AnimationEffect``'s iterations.
    iterations: float

    #: ``AnimationEffect``'s iteration duration.
    #: Milliseconds for time based animations and
    #: percentage [0 - 100] for scroll driven animations
    #: (i.e. when viewOrScrollTimeline exists).
    duration: float

    #: ``AnimationEffect``'s playback direction.
    direction: str

    #: ``AnimationEffect``'s fill mode.
    fill: str

    #: ``AnimationEffect``'s timing function.
    easing: str

    #: ``AnimationEffect``'s target node.
    backend_node_id: typing.Optional[dom.BackendNodeId] = None

    #: ``AnimationEffect``'s keyframes.
    keyframes_rule: typing.Optional[KeyframesRule] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["delay"] = self.delay
        json["endDelay"] = self.end_delay
        json["iterationStart"] = self.iteration_start
        json["iterations"] = self.iterations
        json["duration"] = self.duration
        json["direction"] = self.direction
        json["fill"] = self.fill
        json["easing"] = self.easing
        if self.backend_node_id is not None:
            json["backendNodeId"] = self.backend_node_id.to_json()
        if self.keyframes_rule is not None:
            json["keyframesRule"] = self.keyframes_rule.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AnimationEffect:
        return cls(
            delay=float(json["delay"]),
            end_delay=float(json["endDelay"]),
            iteration_start=float(json["iterationStart"]),
            iterations=float(json["iterations"]),
            duration=float(json["duration"]),
            direction=str(json["direction"]),
            fill=str(json["fill"]),
            easing=str(json["easing"]),
            backend_node_id=(
                dom.BackendNodeId.from_json(json["backendNodeId"])
                if json.get("backendNodeId", None) is not None
                else None
            ),
            keyframes_rule=(
                KeyframesRule.from_json(json["keyframesRule"])
                if json.get("keyframesRule", None) is not None
                else None
            ),
        )


@dataclass
class KeyframesRule:
    """
    Keyframes Rule
    """

    #: List of animation keyframes.
    keyframes: typing.List[KeyframeStyle]

    #: CSS keyframed animation's name.
    name: typing.Optional[str] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["keyframes"] = [i.to_json() for i in self.keyframes]
        if self.name is not None:
            json["name"] = self.name
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> KeyframesRule:
        return cls(
            keyframes=[KeyframeStyle.from_json(i) for i in json["keyframes"]],
            name=str(json["name"]) if json.get("name", None) is not None else None,
        )


@dataclass
class KeyframeStyle:
    """
    Keyframe Style
    """

    #: Keyframe's time offset.
    offset: str

    #: ``AnimationEffect``'s timing function.
    easing: str

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["offset"] = self.offset
        json["easing"] = self.easing
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> KeyframeStyle:
        return cls(
            offset=str(json["offset"]),
            easing=str(json["easing"]),
        )


def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Disables animation domain notifications.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Animation.disable",
    }
    json = yield cmd_dict


def enable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Enables animation domain notifications.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Animation.enable",
    }
    json = yield cmd_dict


def get_current_time(id_: str) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, float]:
    """
    Returns the current time of the an animation.

    :param id_: Id of animation.
    :returns: Current time of the page.
    """
    params: T_JSON_DICT = dict()
    params["id"] = id_
    cmd_dict: T_JSON_DICT = {
        "method": "Animation.getCurrentTime",
        "params": params,
    }
    json = yield cmd_dict
    return float(json["currentTime"])


def get_playback_rate() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, float]:
    """
    Gets the playback rate of the document timeline.

    :returns: Playback rate for animations on page.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Animation.getPlaybackRate",
    }
    json = yield cmd_dict
    return float(json["playbackRate"])


def release_animations(
    animations: typing.List[str],
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Releases a set of animations to no longer be manipulated.

    :param animations: List of animation ids to seek.
    """
    params: T_JSON_DICT = dict()
    params["animations"] = [i for i in animations]
    cmd_dict: T_JSON_DICT = {
        "method": "Animation.releaseAnimations",
        "params": params,
    }
    json = yield cmd_dict


def resolve_animation(
    animation_id: str,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, runtime.RemoteObject]:
    """
    Gets the remote object of the Animation.

    :param animation_id: Animation id.
    :returns: Corresponding remote object.
    """
    params: T_JSON_DICT = dict()
    params["animationId"] = animation_id
    cmd_dict: T_JSON_DICT = {
        "method": "Animation.resolveAnimation",
        "params": params,
    }
    json = yield cmd_dict
    return runtime.RemoteObject.from_json(json["remoteObject"])


def seek_animations(
    animations: typing.List[str], current_time: float
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Seek a set of animations to a particular time within each animation.

    :param animations: List of animation ids to seek.
    :param current_time: Set the current time of each animation.
    """
    params: T_JSON_DICT = dict()
    params["animations"] = [i for i in animations]
    params["currentTime"] = current_time
    cmd_dict: T_JSON_DICT = {
        "method": "Animation.seekAnimations",
        "params": params,
    }
    json = yield cmd_dict


def set_paused(
    animations: typing.List[str], paused: bool
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Sets the paused state of a set of animations.

    :param animations: Animations to set the pause state of.
    :param paused: Paused state to set to.
    """
    params: T_JSON_DICT = dict()
    params["animations"] = [i for i in animations]
    params["paused"] = paused
    cmd_dict: T_JSON_DICT = {
        "method": "Animation.setPaused",
        "params": params,
    }
    json = yield cmd_dict


def set_playback_rate(
    playback_rate: float,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Sets the playback rate of the document timeline.

    :param playback_rate: Playback rate for animations on page
    """
    params: T_JSON_DICT = dict()
    params["playbackRate"] = playback_rate
    cmd_dict: T_JSON_DICT = {
        "method": "Animation.setPlaybackRate",
        "params": params,
    }
    json = yield cmd_dict


def set_timing(
    animation_id: str, duration: float, delay: float
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Sets the timing of an animation node.

    :param animation_id: Animation id.
    :param duration: Duration of the animation.
    :param delay: Delay of the animation.
    """
    params: T_JSON_DICT = dict()
    params["animationId"] = animation_id
    params["duration"] = duration
    params["delay"] = delay
    cmd_dict: T_JSON_DICT = {
        "method": "Animation.setTiming",
        "params": params,
    }
    json = yield cmd_dict


@event_class("Animation.animationCanceled")
@dataclass
class AnimationCanceled:
    """
    Event for when an animation has been cancelled.
    """

    #: Id of the animation that was cancelled.
    id_: str

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AnimationCanceled:
        return cls(id_=str(json["id"]))


@event_class("Animation.animationCreated")
@dataclass
class AnimationCreated:
    """
    Event for each animation that has been created.
    """

    #: Id of the animation that was created.
    id_: str

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AnimationCreated:
        return cls(id_=str(json["id"]))


@event_class("Animation.animationStarted")
@dataclass
class AnimationStarted:
    """
    Event for animation that has been started.
    """

    #: Animation that was started.
    animation: Animation

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AnimationStarted:
        return cls(animation=Animation.from_json(json["animation"]))


@event_class("Animation.animationUpdated")
@dataclass
class AnimationUpdated:
    """
    Event for animation that has been updated.
    """

    #: Animation that was updated.
    animation: Animation

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AnimationUpdated:
        return cls(animation=Animation.from_json(json["animation"]))
