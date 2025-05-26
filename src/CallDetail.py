from src.utils import parse_phone_number, parse_iso_datetime, parse_time_duration, parse_call_memo, classify_number
from src.idn_area_codes import EMERGENCY_NUMBERS
import math
from src.utils import call_hash, classify_number, format_datetime_as_human_readable, format_timedelta, format_username, parse_call_memo, parse_iso_datetime, parse_phone_number

class CallDetail:
    def __init__(
        self,
        sequence_id: str,
        user_name: str,
        call_from: str,
        call_to: str,
        call_type: str,
        dial_start_at: str,
        dial_answered_at: str,
        dial_end_at: str,
        ringing_time: str,
        call_duration: str,
        call_memo: str,
        call_charge: str,
    ):
        self.sequence_id = sequence_id
        self.user_name = user_name
        self.call_from = parse_phone_number(call_from)  # Normalizing here
        self.call_to = parse_phone_number(call_to)      # Normalizing here
        self.call_type = call_type
        self.dial_start_at = parse_iso_datetime(dial_start_at)
        self.dial_answered_at = (
            parse_iso_datetime(dial_answered_at) if dial_answered_at != "-" else None
        )
        self.dial_end_at = parse_iso_datetime(dial_end_at)
        self.ringing_time = parse_time_duration(ringing_time)
        self.call_duration = parse_time_duration(call_duration)
        self.call_memo = parse_call_memo(call_memo)
        self.call_charge = self.calculate_call_charge()
        self.number_type = classify_number(self.call_to, self.call_type, self.call_from, self.call_to)

    def calculate_call_charge(self) -> str:
        number_type = classify_number(self.call_to, self.call_type, self.call_from, self.call_to)
        if self.call_type in ["Internal Call", "Internal Call (No answer)", "Monitoring"]:
            return "0"

        if str (self.call_to) == "30000328": #body factory
            duration_in_minutes = self.call_duration.total_seconds() / 60
            call_charge = rounded_duration * 1350
            return str(call_charge)

        elif self.call_type not in ["OUTGOING_CALL", "Outbound call", "PREDICTIVE_DIAL", "AUTOMATIC_TRANSFER"]: # Delete this part for those need inbound calculation
            return "0" # or some other default value
        else:
            if number_type in ["Premium Call", "Toll-Free", "Split Charge"] or number_type in EMERGENCY_NUMBERS.values():
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 1700
            elif number_type in {"International - AUT (PSTN)", "International - DNK (PSTN)", "International - NLD (PSTN)", 
            "International - NZL (PSTN)", "International - NOR (PSTN)", "International - ESP (PSTN)", "International - CHE (PSTN)"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 1000
            elif number_type in {"International - ITA (PSTN)", "International - SGP", "International - TWN (PSTN)", "International - THA"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 1250
            elif number_type in {"International - ARG (PSTN)", "International - CHN", "International - DEU (PSTN)", "International - HKG", "International - JPN (PSTN)", "International - USA/CAN"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 1500
            elif number_type in {"International - MYS"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 1750
            elif number_type in {"International - KOR"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 2000
            elif number_type in {"International - CRI"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 2250
            elif number_type in {"International - FRA (PSTN)", "International - MEX"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 2500
            elif number_type in {"International - LAO"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 2750
            elif number_type in {"International - IND", "International - TWN (Mobile)", "International - GBR (PSTN)"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 3000
            elif number_type in {"International - AUS", "International - JPN (Mobile)"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 3250
            elif number_type in {"International - NLD (Mobile)", "International - ESP (Mobile)", "International - TUR (PSTN)", "International - ARE"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 3500
            elif number_type in {"International - BRA (PSTN)", "International - FRA (Mobile)", "International - PHL"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 4000
            elif number_type in {"International - NZL (Mobile)", "International - TUR (Mobile)"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 4250
            elif number_type in {"International - DNK (Mobile)", "International - DOM", "International - DEU (Mobile)", "International - ISL"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 4500
            elif number_type in {"International - AUT (Mobile)", "International - NOR (Mobile)"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 4750
            elif number_type in {"International - VNM"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 5000
            elif number_type in {"International - ARG (Mobile)"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 5250
            elif number_type in {"International - CHE (Mobile)"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 5500
            elif number_type in {"International - RUS", "International - ZAF", "International - GBR (Mobile)"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 5750
            elif number_type in {"International - UKR"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 6250
            elif number_type in {"International - KHM", "International - MMR"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 6750
            elif number_type in {"International - ARM", "International - AZE (PSTN)", "International - ITA (Mobile)"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 7000
            elif number_type in {"International - AZE (Mobile)", "International - BLR"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 7500
            elif number_type in {"International - BRA (Mobile)"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 8250
            elif number_type in {"International - GEO (PSTN)"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 9000
            elif number_type in {"International - GEO (Mobile)"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 11500
            elif number_type in {"International - CUB"}:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 17250
            else:
                duration_in_minutes = self.call_duration.total_seconds() / 60
                rounded_duration = math.ceil(duration_in_minutes)
                call_charge = rounded_duration * 720
            return str(call_charge)

    def to_dict(self) -> dict:
        return {
            "Sequence ID": self.sequence_id,
            "User name": format_username(self.user_name),
            "Call from": self.call_from,
            "Call to": self.call_to,
            "Call type": self.call_type,
            "Number type": classify_number(self.call_to, self.call_type, self.call_from, self.call_to),
            "Dial starts at": format_datetime_as_human_readable(self.dial_start_at),
            "Dial answered at": format_datetime_as_human_readable(
                self.dial_answered_at
            ),
            "Dial ends at": format_datetime_as_human_readable(self.dial_end_at),
            "Ringing time": format_timedelta(self.ringing_time),
            "Call duration": format_timedelta(self.call_duration),
            "Call memo": self.call_memo,
            "Call charge": self.call_charge,
        }

    def hash_key(self) -> str:
        return call_hash(self.call_from, self.call_to, self.dial_start_at)